# Day 6

As for day 6, you need to prepare a dictionary that hold `timer: n_fish` where the `timer` is the input that were given for the puzzle, and `n_fish` is the number of timer inside the input. This is to make it easier for us to loop through the fishes. For this, we are going to use `defaultdict` from collections module.

```python
def update_fish(fishes):
    new_fish_lib = defaultdict(int)
    for timer, n_fish in fishes.items():
        if timer == 0:
            timer = 7
            new_fish_lib[8] += n_fish
        new_fish_lib[timer - 1] += n_fish
    return new_fish_lib
```

The function above will create a new dictionary with default value of integer that will store informations about our fishes. For today puzzle, the solution is much more simple since both task require you to do the same thing. You just need to give the number of days as specify by the puzzle into the function below.

```python

def solution(fishes, days):
    fish_lib = fishes.copy()
    for _ in range(days):
        fish_lib = update_fish(fish_lib)

    return sum(fish_lib.values())

```

The function above create a copy of fishes dictionary to avoid changes to the original dictionary. Then it will update that dictionary for `n=days` times. Lastly it will return the sum of the values from the last updated fishes dictionary.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
