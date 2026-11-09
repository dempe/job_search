// Renders a table of the applications with one derived status, for Applications.md:
//
//   await dv.view("_meta/scripts/applications", {status: "rejected", columns: ["applied", "source", "interviews"], sort: "desc"})
//   await dv.view("_meta/scripts/applications", {followUp: true, columns: ["ago", "source"]})
//
// Status isn't stored. It's derived, in this order:
//   1. the application's `outcome`, set by hand for what no interview note records
//      (rejected before interviewing, declined, offer, cancelled)
//   2. an interview note's `outcome`: rejected, declined, offer, ghosted, in that order
//   3. with interview notes: ghosted if the latest is still pending or advanced 30 days
//      after its date, otherwise interviewing
//   4. without: awaiting-reply for 30 days after applying, then ghosted
// `follow_up: true` is a reminder, listed only while the status is awaiting-reply or ghosted.
//
// Dates come from file.frontmatter: an interview note's practice sessions have
// `date::` fields that Dataview merges into its page-level `date`.

const { DateTime } = dv.luxon;
const today = DateTime.now().startOf("day");
const GHOST_DAYS = 30;

function day(value) {
  if (!value) return null;
  if (DateTime.isDateTime(value)) return value.startOf("day");
  if (value instanceof Date) return DateTime.fromJSDate(value).startOf("day");
  const match = String(value).match(/^\d{4}-\d{2}-\d{2}/);
  return match ? DateTime.fromISO(match[0]) : null;
}

const daysSince = (date) => Math.floor(today.diff(date, "days").days);

function interviews(app) {
  return app.file.inlinks
    .filter((link) => link.path.includes("/Interviews/"))
    .map((link) => dv.page(link.path))
    .filter((page) => page && page.type === "interview")
    .map((page) => ({ date: day(page.file.frontmatter.date), outcome: page.file.frontmatter.outcome }))
    .array();
}

function status(app) {
  if (app.file.frontmatter.outcome) return app.file.frontmatter.outcome;
  const ivs = interviews(app);
  const outcomes = ivs.map((iv) => iv.outcome);
  for (const outcome of ["rejected", "declined", "offer", "ghosted"]) {
    if (outcomes.includes(outcome)) return outcome;
  }
  if (ivs.length) {
    const latest = ivs.reduce((a, b) => (b.date && (!a.date || b.date > a.date) ? b : a));
    const stale = ["pending", "advanced"].includes(latest.outcome) && latest.date && daysSince(latest.date) > GHOST_DAYS;
    return stale ? "ghosted" : "interviewing";
  }
  const applied = day(app.file.frontmatter.applied);
  return applied && daysSince(applied) <= GHOST_DAYS ? "awaiting-reply" : "ghosted";
}

function ago(app) {
  const applied = day(app.file.frontmatter.applied);
  if (!applied) return null;
  const days = daysSince(applied);
  if (days === 0) return "today";
  const weeks = Math.floor(days / 7);
  const parts = [];
  if (weeks) parts.push(`${weeks} week${weeks === 1 ? "" : "s"}`);
  if (days % 7) parts.push(`${days % 7} day${days % 7 === 1 ? "" : "s"}`);
  return `${parts.join(", ")} ago`;
}

const COLUMNS = {
  applied: ["Applied", (app) => app.applied],
  ago: ["Applied", ago],
  source: ["Source", (app) => app.source],
  contract: ["Contract", (app) => app.contract],
  interviews: ["Num Interviews", (app) => interviews(app).length],
};

const columns = input.columns.map((name) => COLUMNS[name]);
const rows = dv
  .pages('"Applications"')
  .where((app) => app.type === "job")
  .where((app) =>
    input.followUp
      ? app.file.frontmatter.follow_up === true && ["awaiting-reply", "ghosted"].includes(status(app))
      : status(app) === input.status
  )
  .sort((app) => day(app.file.frontmatter.applied)?.toMillis() ?? 0, input.sort ?? "asc");

dv.table(
  ["Application", ...columns.map(([header]) => header)],
  rows.map((app) => [app.file.link, ...columns.map(([, value]) => value(app))])
);
