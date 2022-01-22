# Day 3

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

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
