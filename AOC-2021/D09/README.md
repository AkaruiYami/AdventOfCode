# Day 9

For Puzzle 1, the task ask us to find the total risk level but adding 1 to the low point's height. Therefore, first we need to find these low points. As mention in the task given, low point is a point where it is lower that its adjacents. So first we loop through the heightmap, and check of the adjacents of the current point is lower than its adjacents, if it is, we then add it to our `total_risk`.

For Puzzle 2, we just need to expand our low points until it reach the `boundary` of the basin. The boundary is a point which the height of 9 and point outside the heightmap. From the low point, we check if the adjacent is a valid basin area. If it is, we then add that point into the `edge_points` list so we can come back to that point and check its adjacents. After we done checking for all adjacents for out current point, we then register this point in a set called `basins_point`. We then continue to check for the next point form our `edge_points` list but if that particular point already exist in `basins_point` we simply skip the process since we already done with that point.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
