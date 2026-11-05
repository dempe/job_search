---
type: interview
application: "[[Applications/Meta (2)]]"
company: Meta (2)
round: 1
date: 2025-04-23 10:30
interviewers:
outcome: rejected
title: Meta (2) - Interview 1
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

## Tech Screen


### Prob 1

You are given an input array, `input` of digits (e.g., `[2, 4, 10, 11, 17, 21]`). You need to output the comma-delimited string of all the digits *not* contained in `input` up to `99`. If more than two consecutive digits are absent, they need to be indicated with a hyphen (e.g., ` 12-16 `). So for the provided example, the output should be `"0,1,3,5-9,12-16,18-20,22-99"`

My solution:

```python
def build_str(input: [str]) -> str:
	out = helper(0, input[0])
	for num1, num2 in zip(input[1:len(input) - 1], input[2:len(input) - 1]):
		out += helper(num1, num2)
	out += helper(input[-1], 99)
	return out

# Assume i < j	
def helper(i: int, j: int) -> str:
	if j - i > 2:
		return f"{i}-{j}"
	out = ""
	for k in range(i, j + 1):
		out += f",{k}"
	return out
```

```python
def build_str(input: [int]) -> str:
	def helper(i: int, j: int) -> [str]:
		if j < i:
			raise ValueError(f"i should be less than j. Found i={i}, j={j})
		if j - i > 2:
			return [f"{i}-{j}"]
		
		out = []			
		for k in range(i, j + 1):  # Should not execute if i == j
			out.append(str(k))
		return out
		
	missing = [i for i in range(100) if i not in set(input)]
	
	start = stop = 0
	prev = -2
	in_seq = False
	out = []
	for num in missing:
		if num != prev + 1 and not in_seq:
			start = num
			in_seq = True
		elif num != prev + 1 and in_seq:
			stop = prev 
			in_seq = False
			out += helper(start, stop)
		prev = num
			
	return ",".join(out)
```

Correct solution from ChatGPT:

```python
def build_missing_ranges(input):
#    missing = [i for i in range(100) if i not in set(input)]
	missing = sorted(set(range(100)) - set(input))

    if not missing:
        return ""

    result = []
    start = prev = missing[0]

    for num in missing[1:] + [None]:  # Add sentinel
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                result.append(str(start))
            elif start + 1 == prev:
                result.append(f"{start},{prev}")
            else:
                result.append(f"{start}-{prev}")
            start = prev = num

    return ",".join(result)
```

### Prob 2

You are a delivery truck driver. Your truck has an overall integer `capacity` that indicates its weight limit. In addition to `capacity`, you are given an array, `trips`, of trips such that each trip is a three element array, `[weight, start, end]`, where `weight` is the weight of the package, and `start` and `end` are where the trip starts and stops. So an overall `trips` array might be `[[4, 1, 5], [3, 2, 6], [6, 1, 2]]`. Note, the trips array is not sorted-you have to determine the best order. Return `True` if it is possible to arrange `trips` in such an order that the packages never exceed `capacity`, `False` otherwise.

Solution I gave:

```python
def is_possible(trips, capacity):
	trips.sort(key=1)
	
	for trip1, trip2 in zip(trips, trips[1:]):
		cap1 = trip1[0]
		cap2 = trip2[0]
		
		if cap1 > capacity or cap2 > capacity:
			return False
		if trip1[1] > trip2[1] and cap1 + cap2 > capacity:
			return False
			
	return True
```

Interviewer said I had the "right idea", but my solution does not pass all cases, because it only ever compares adjacent trips in the array. But more than two trips can overlap, so current weight can be the sum of more than two weights. My solution never checks this case.

E.g., `[[2, 2, 100], [2, 2, 5], [2, 4, 5]]` where `capacity = 5`. My solution would return `True`, but the correct answer is `False`, because the three trips overlap between `[4, 5]`, where the total weight at the point is 6. `6 > 5`
