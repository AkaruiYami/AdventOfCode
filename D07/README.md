# Day 7

After collecting the necessary information, you can loop from 0 until halve of the maximum position and stores the sum of step requires to reach to that point for each crab submarine. Then from the list you created, you can then return the minimum value.

As for the puzzle 2, instead of storing the step, what you need is to use arithmatic progression since the command difference for each step is contant 1. The formula is `S = n(a+L)/2` where n is steps, a is the initial value (which is 1), and L is the last value (which is the same as steps).

```python
    (abs(new_pos - current_pos) * (1 + abs(new_pos - current_pos))) // 2
```

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
