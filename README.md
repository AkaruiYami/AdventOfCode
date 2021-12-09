![AoC2021-AkaruiYami-Youtube-Series](https://scontent.fkul3-2.fna.fbcdn.net/v/t39.30808-6/263090987_198128025857818_3390643286314791789_n.png?_nc_cat=102&ccb=1-5&_nc_sid=730e14&_nc_ohc=3gk1fwzU_7gAX9fwoDe&tn=ltBEoBUIPQB7JKmb&_nc_ht=scontent.fkul3-2.fna&oh=633fcbba405e269f2a256fafc51458ff&oe=61B3A0EA)

# My Attempt in AoC 2021.

Each daily challenges including nessecary input will be keep inside a folder.
`D01` is for challenge from day 1.

You can checkout my YouTube Video for AoC Series:\
[AoC 2021 YouTube Playlist](https://www.youtube.com/watch?v=Invlu2HLcBA&list=PLMzyOn0orr7zDnq32QlDgo0nAGbU-2K2A)

## Day 1

The puzzle is quite simple. You only need to count how many times the given input increases compare to previous input. So basically, You just create a new list that contains booleans. It is true if the current input is greater than previous input.

Second puzzle is also quite simple. You just need to prepare the given list of input. Basically, you just need to create new list of input and pass it to function from solution 1 since the concept is the same but the only different is the input uses to compare between current and previous input.

## Day 2

For this set of puzzle, You create a special function to obtain a set of instructions from given list of input by splitting it to two part, `command` and `value`. Then you just need to check the `command`. If it forward, then add the respactive variable to the given `value`.

The second part of the puzzle is really similar to the first one, but there is a new variable that needed to be add into the function.

## Day 3

For this puzzle, you need to find `gamma_rate` first. From there, you can just flip `gamma_rate` using `XOR` so that you get `epsilon_rate`.
To find `gamma_rate`, first you need to loop through each bit of the binary numbers to find the most common bit.

```python
gamma_bit = sum((_l >> i) & 1 for _l in l) > len(l) // 2
```

As you can see, the code above is to find the most common bit, by adding up all `1's` and compare it to the lenght of binary report. If the sum is greater than the length of binary report, therfore we know that 1 is the most common, so that line of code should return `True` which is `1`.

```python
gamma_rate |= gamma_bit << i
```

The code above will add the result into `gamma_rate`.

For puzzle 2, it is a bit of hasle. First you need to make a copy of binary report since you are going to discard the item that does not fit the requirment.
To find the most common, we can reuse the same line of code that we use for finding gamma_rate but with minor adjustment.

```python
o2_bit = sum((\_l >> (n_bit - i)) & 1 for \_l in o2_l) >= len(o2_l) / 2
```

First, instead of checking the bit from right, we check the bit from the left. That is why we have `(n_bits - i)`.
Then we just need to update our list.

```python
    o2_l = [_l for _l in o2_l if (_l >> (n_bit - i)) & 1 == o2_bit] or o2_l
```

For `co2` we can do the same but instead greater than length of report, we find if it is lesser then the length of report.

```python
    co2_bit = sum((_l >> (n_bit - i)) & 1 for _l in co2_l) < len(co2_l) / 2
```

## Day 4

After analysing the input, you will see that the first line from the input is a set of numbers separated by comma. Therefore, you can get the first important variable which is `draws` as a list of str numbers. Then to get board, you need to read first 5 lines after finding an empty string since each board is separated by a new line.

After getting all important variables, `draws` and `boards`, you can start build your `Board` class so that you can manipulate the boards much easier. There, you can create several methods, `check_for_win`, `mark`, and `get_score`. Don't forget to create a copy of the board data so that you can reset the board after marking the data. To mark a data, I simply change the data to `"X"` since the marked data are not really important. We only need to know that it was already marked.

From there, we can calculate the score collecting all remaining unmarked data and multpy it with the last drawn number.

```python
        return sum(int(data) for data in _flatten_data if data != "X") * int(last_draw)
```

As you can see, marked data can be ignore by using if statement.

To find the first winner, you just need to return the score after finding the first winner. To find last winner, simply discrad the winning board from a copy of board list until none remain inside that list. The last item that was discarded is the last winner.
