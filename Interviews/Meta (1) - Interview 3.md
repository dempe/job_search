---
type: interview
application: "[[Job Applications/Meta (1)]]"
company: Meta (1)
round: 3
date: 2023-10-19
interviewers:
outcome: rejected
title: Meta (1) - Interview 3
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

It went better than my mock interview! And I hadn't seen either Q before.

### Check if String is Palindrome given that We Are Able to Remove 1 Element

I wasn't sure how to solve this at first, so I just implemented a basic `isPalindrome(String s)` function first:

```Java
public function boolean isPalindrome(final String s) {
	final int len = s.length;
	
	for (int I = 0; I < len / 2; i++) {
		final char1 = s[i];
		final char2 = s[len - 1 - i];

        // In the interview, I acutally put a check in to see if I and len - 1 - I were equal.  This is completely retarded and makes no sense.


		if (char1 != char2) {
			return false;
		}
	}

	return true;
}
```

Then modified it to be able to remove one element:

```Java
public function boolean isPalindrome(final String s, boolean haveRemoved) {
	final int len = s.length;
	
	for (int I = 0; I < len / 2; i++) {
		final char1 = s[i];
		final char2 = s[len - 1 - i];

        // In the interview, I acutally put a check in to see if I and len - 1 - I were equal.  This is completely retarded and makes no sense.

		if (char1 != char2 && haveRemoved == false) {
			final String s1 = s.remove(i);
			final String s2 = s.remove(len - 1 - i);
			
			return isPalindrome(s1, true) || isPalindrome(s2, true);
		}
		if (char1 != char2 && haveRemoved == true) {
			return false;
		}
	}

	return true;
}
```

Can also be extended to be able to remove up to $k$ elements by making `haveRemoved` an integer and passing in a max removal integer, `k`.

Runtime: $O(n)$ — we need to check each element.

### Find the Longest Consecutive Subsequence (s) of a String and return a List of One Element from Each

This was tricksey and we ran out of time we did.
