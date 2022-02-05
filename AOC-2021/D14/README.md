# Day 14

For this puzzle what we can do is scan for the pair and insert the character between it and continue checking the if any pair exist in given string. This method will require so much time after couple of iteration because the string will end up pretty long. Therefore, we are going to sacrifice some spaces to make the operation time shorter.

What we need are 2 dictionary that will hold `pair count` and `character count`. For this, we are going to need to import some module to help us count the item for us. First, we import `Counter` and `defaultdict` both from `collection` module.

For `character count` we create a defaultdict that expected `int` for it values. We initialize our `chars_count` with the give string. So now, `chars_count` will have a `string` as its key and `int` as its value. The string is the character that exist in our current input string or we call it template in this puzzle.

For `pair count` we create a dictionary that will hold the every possible pair from given string and the count of that pair. We use Counter class to help us contruct this dictionary.

Now what we need is a function that will scan our data and update our respective dictionary. In this function, we first create a temporary dictionary that expecting an `int` as its value. So we once again use defaultdict. The we loop through our `pair_count` items.

```python
for pair, count in pairs_count.items():
        chars_count[rules[pair]] += count
        temp[(pair[0], rules[pair])] += count
        temp[(rules[pair], pair[1])] += count
```

If we look at the code above, we see that in the loop, we first update our `chars_count` dictionary with the count of the new inserted character. Note that variable `rules` is actually a dictionary of target pair and new character.

Then we update our temporary dictionary with the newly created pair and it count. When we insert a new character between 2 letter, we actually create 2 new pair. For example, we insert "C" in between "AB", we get "ACB". In another world, we have new pair which is "AC" and "CB". That is why we update `temp` twice. Once for the first part and then for the second part.

After that we will return our `temp`. Note that we add `count` because there might be some duplicate pair inside our string.

Since the puzzle ask for the difference between max count and min count, we will use built-in function `max()` and `min()` to retrieve those value from our `chars_count` dictionary.

[<sup>< main page](../README.md#My-Attempt-in-AoC-2021)
