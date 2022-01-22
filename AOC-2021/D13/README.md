# Day 13

First, we need to extract the important information from the input. The input has 2 sections, `list of dots` and `fold instructions`. For this, we can use `re` module. Below is the pattern that we can use to identify `fold instructions` We will capture on what axis it is and at what point the axis will be.

```python
    fold_instructions_pattern = re.compile(r"fold along ([xy])=(\d+)")
```

Next we will create a function to move our dots. The formula is simple, every dots that are below or at the right of the fold axis will be move toward the axis twice the distance between them. Basically, the formula is `dot_origin + 2 * (axis - dot_origin)`. To make sure that we only move the dots that are on movinf side, we can use buil-in function `min` since all the dots coordinate that located on moving side will always greater than the axis coordinate. Therefore, if `(axis - dot_origin) < 0` the dot is on moving side else if `(axis - dot_origin) >= 0` the dot is outside of moving side.

For solution 1, we just move the dots only once by following the very first `fold instruction` and return the `len` of the dots list.

For solution 2, we need to move the dots all the way until we follows all of the `fold instruction` then we need to draw the dots. By drawing the dots, we will then get the `code` that the task asking you for. Below is the function that responsible to draw the dots. We simply look for the `max` `x` and `y` from out dots and loop through them. if the `(x, y)` is in dots, then we will print them using `fill_char` to shows that there is a dot there.

```python
def draw_map(dots, fill_char="#", empty_char="."):
    width = max(dot[0] for dot in dots)
    height = max(dot[1] for dot in dots)
    for y in range(height + 1):
        row = ""
        for x in range(width + 1):
            row += fill_char if (x, y) in dots else empty_char
        print(row)
```

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
