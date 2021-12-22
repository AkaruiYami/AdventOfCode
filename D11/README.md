# Day 11

We have an 10x10 energy grid. Therefore we have a 2D list.

For puzzle 1, first we increase all energy by 1 if the energy is lower than 9. If the current energy is greater and equal to 9, then we just set it to 0. After increasing the energy level, we need to find all 0 inside the energy grid and return the coordinate of the grid. Then we can process this flash point by increasing the surrounding point by 1 if the current energy of the surrounding points is lower than 9, else set it to 0. After that we check if the new energy level for the surrounding points is 0. If it is, then we append that point coordinate into our flash point list so we can process it later on. After we done processing the current point, we need to add the point into a set so we know that we already process that particular point.

For puzzle 2, we just need to loop our process unti we reach the point where all energy inside our energy grid are 0. We can reause our previous 3 functions to increase step, update adjacents, find flash. Create a new function or just a simple lambda function that will return True if all value inside our energy grid is 0. Below is the lambda function that do just that:

```python
    is_all_flashed = lambda e: all([0 in set(e_r) and len(set(e_r)) == 1 for e_r in e])
```

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
