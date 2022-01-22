# Day 5

So, this puzzle is a bit simple. First you prepare the data. In this case, I decide to create a list of lines where each line is a list of points. For puzzle 1, you only need to consider the line where `x1 == x2` or `y1 == y2`. Then these lines will then registered to a dictionary that hold all point inside `world` or `plane`.

```python
get_step = lambda l: 0 if l[0] == l[1] else (l[1] - l[0]) / abs(l[1] - l[0])
```

Lambda function above are use to calculate the direction of axis. If the line is a horizontal line, then the direction for `x-axis` is `0`. If the line is a vertical line, then the direction for `y-axis` will be `0`. If the `end point` is behind `start point`, then the direction for the respective axis will be `-1`. After getting the direction of the line, we can then calculte the distance of the line by adding the absolute value of the difference between two points.

```python
    distance = abs(end[0] - start[0]) + abs(end[1] - start[1])
```

Then, we will update our `world dictionary`. The dicrionary will hold the `coordinate of point` on imaginary plain and the value is `the number of times a line went through the point`.

```python
for i in range(distance + 1):
        x = start[0] + i * x_step
        y = start[1] + i * y_step
        world[(x, y)] += 1
```

After that, we just need to count, how many point inside the world dictionary that the value is greater than 1.

For puzzle 2, there is a minor adjustment that we need to make. Instead of adding two absolute value of the difference between two points, we find the max value between `x2-x1` and `y2-y1`

```python
    distance = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
```

This is because, for diagonal line, the result from `x2-x1` and `y2-y1` will both return exact same result which is double our distance. The previous code can be use for puzzle 1 because one of two axis will return 0. We took the max value because for horizontal line, `x2-x1` will return 0 but `y2-y1` while return some value which will surely be greater than 0. It is the same for vertical line but vise versa.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
