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
