# Day 12

First thing first, we need to get our cave map. Basically, we will use `defaultdict` from `collections` module where we will set the default value of our dictionary to `set` because we don't want to have any duplication in our cave connections. We will have a dictionary of `cave entry` and `cave connections` for it key and value.

Noted, we can exclude `end` from our cave entry since it is the end of the journey and we also will not include `start` to cave connections because we sould not return back to `start`.

After we prepare our cave map, now we can make a new function that will look trough all possible path and return 1 if the path reach to the end but if it reach to dead end, it will return 0. We know it is a dead end if the next location is a small cave and it already exist in our travelled path list.

```python
def travel(cave_map, curr_loc="start", travelled_path=None):
    if travelled_path is None:
        travelled_path = list()

    if curr_loc == "end":
        return 1

    # check if we visit small cave
    if curr_loc.islower() and curr_loc in travelled_path:
        return 0

    travelled_path.append(curr_loc)

    count = 0
    for loc in cave_map[curr_loc]:
        count += travel(cave_map, loc, travelled_path.copy(), reapeatable)

    return count
```

Function above will return total number of path that able to reach to the `end`. As you can see, we are using recursive function. Note, we need to pass a copy of `travelled_path` so that we will not change the original list.

For puzzle 2, we just need to add a new parameter to our already existing function as below:

```python

def travel(cave_map, curr_loc="start", travelled_path=None, repeatable=False):
    if travelled_path is None:
        travelled_path = list()

    if curr_loc == "end":
        return 1

    # check if we visit small cave
    if curr_loc.islower() and curr_loc in travelled_path:
        if repeatable:
            repeatable = False
        else:
            return 0

    travelled_path.append(curr_loc)

    count = 0
    for loc in cave_map[curr_loc]:
        count += travel(cave_map, loc, travelled_path.copy(), repeatable)

    return count

```

Then we will say that `repeatable=True` so that the function knows that the small cave is actually repeatable and then set the variable back to False. This is to make sure that the small can only be repeated only once.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
