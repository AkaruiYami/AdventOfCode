import os
from collections import Counter, defaultdict


def read_data(raw_data):
    """Return a tupple of data containing template and rules

    Args:
        raw_data (list[str]): A list of string containing a template and rules.

    Returns:
        tuple[str, dict[tuple[str]: str]]: A tuple of template and rules.
    """
    raw_data = list(filter(None, raw_data))
    template = raw_data.pop(0)

    cleanse = lambda s: s.strip()
    rules = [tuple(map(cleanse, rule.split("->"))) for rule in raw_data]
    rules_dict = {tuple(key): value for key, value in rules}

    return template.strip(), rules_dict


def insert_chars(pairs_count, chars_count, rules):
    """Insert a character in between matching pairs and update the characters count.

    Args:
        pairs_count (dict[tuple[str]: int]): A dictionary containing all possible pairs as it keys and the count.
        chars_count (dict[tuple[str]: int]): A dictionary containing all characters and its count.
        rules (dict[tuple[str]: str]): A dictionary that containing the set of rules where to insert the character.

    Returns:
        dict[tuple[str]: str]: A dictionary containing all possible pairs as it keys and the count.
    """
    temp = defaultdict(int)
    for pair, count in pairs_count.items():
        chars_count[rules[pair]] += count
        temp[(pair[0], rules[pair])] += count
        temp[(rules[pair], pair[1])] += count
    return temp


def solution(data, n):
    """Get the solution for the puzzle.

    Args:
        data (tuple[str, dict[tuple[str]:str]]): A set of template and rules.
        n (int): The number of steps to process the character insertions.

    Returns:
        int: Most common character - least common character.
    """
    template, rules = data
    chars_count = defaultdict(int, Counter(template))
    pairs_count = Counter(zip(template, template[1:]))
    for _ in range(n):
        pairs_count = insert_chars(pairs_count, chars_count, rules)
    return max(chars_count.values()) - min(chars_count.values())


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = read_data(file.read().splitlines())
    print(solution(data, 10))
    print(solution(data, 40))
