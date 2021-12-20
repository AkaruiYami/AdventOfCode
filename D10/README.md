# Day 10

For the first solution, you create an empty dictionary that will store the `corrupted line index` and `illegal character`. This dictionary can be use to determine what the illegal character are for solution 1 and can later be use to discard all corupted lines for solution 2.

The idea was to loop through each character and if the character is an `opening character` then we will append it into a list. If the character is a `closing character`, then we will took out the last `opening character` and compare it if they are a legal pair. If not, we can break the current loop for the current line and append the illegal character into our dictionary. Finally we just need to calculate the total syntac error score acording to the score table provided.

For puzzle 2, after we look for corrupted lines, we can discarded those lines. What left is incomplete lines.

```python
incomplete_lines = [
        x for ix, x in enumerate(lines) if ix not in corrupted_brackets.keys()
    ]
```

Then we are going to find the missing pair. Note, when appending the missing character into `missing_pairs` list, we need to reverse the loop.

```python
missing_pair.append([pair_table[x] for x in open_brackets[::-1]])
```

Then finally, we calculate the scores for each lines. Sort the scores list and return the score that located at index half of the list length as below:

```python
    scores = list()
    for line in missing_pair:
        score = 0
        for x in line:
            score = score * 5 + point_table[x]
        scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]
```

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
