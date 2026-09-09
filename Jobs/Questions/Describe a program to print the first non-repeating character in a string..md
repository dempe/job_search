---
type: question
times_asked: 1
technical: true
title: Describe a program to print the first non-repeating character in a string.
date_created: "2023-05-30 15:37"
date_modified: "2025-05-31 13:30"
---

I don't think it's possible to do this without looping over the string twice, but my naive solution is the following.

1. Initialize hash map of char to ints.
2. Loop over each char in str
3. If char not in hash map, add it with a value of 1
4. If char is in hash map, increment it
5. Loop over str again checking each char in the hash map
6. If a char's value in the hash map is 1, return that char

Runtime 2n, O (n). Space complexity O (n).

You could use a bi-directional hash map and search for `1`, but that won't guarantee order. However, I think we could use the returned set of characters that appear once to at least reduce the runtime (though, not asymptotically). Even if this worked, we'd still be at O (n), so I think this is moot.

If we know ahead of time, what character set we are dealing with, we could reduce the space complexity. For example, if we are only dealing with ASCII characters:

```python
def first_non_repeating_character(string):
    character_frequency = [0]*128  # assuming ASCII characters

    # Count frequency of each character
    for char in string:
        character_frequency[ord(char)] += 1

    # Find the first non-repeating character
    for char in string:
        if character_frequency[ord(char)] == 1:
            return char

    return None
```

Runtime 2n, O (n). Space complexity O (1).

A similar approach could be used for larger character sets, but Unicode is huge, so would probably be better to just stick with the original.

## Asked by

- Unknown (2021)
