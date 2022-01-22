# Day 4

After analysing the input, you will see that the first line from the input is a set of numbers separated by comma. Therefore, you can get the first important variable which is `draws` as a list of str numbers. Then to get board, you need to read first 5 lines after finding an empty string since each board is separated by a new line.

After getting all important variables, `draws` and `boards`, you can start build your `Board` class so that you can manipulate the boards much easier. There, you can create several methods, `check_for_win`, `mark`, and `get_score`. Don't forget to create a copy of the board data so that you can reset the board after marking the data. To mark a data, I simply change the data to `"X"` since the marked data are not really important. We only need to know that it was already marked.

From there, we can calculate the score collecting all remaining unmarked data and multpy it with the last drawn number.

```python
        return sum(int(data) for data in _flatten_data if data != "X") * int(last_draw)
```

As you can see, marked data can be ignore by using if statement.

To find the first winner, you just need to return the score after finding the first winner. To find last winner, simply discrad the winning board from a copy of board list until none remain inside that list. The last item that was discarded is the last winner.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
