import os


def solution1(l, n_bit):
    gamma_rate = 0
    for i in range(n_bit):
        gamma_bit = sum((_l >> i) & 1 for _l in l) > len(l) // 2
        gamma_rate |= gamma_bit << i
    epsilon_rate = gamma_rate ^ int("1" * n_bit, 2)
    return gamma_rate * epsilon_rate


def solution2(l, n_bit):
    o2_l = l.copy()
    co2_l = l.copy()

    for i in range(n_bit):
        o2_bit = sum((_l >> (n_bit - i)) & 1 for _l in o2_l) >= len(o2_l) / 2
        o2_l = [_l for _l in o2_l if (_l >> (n_bit - i)) & 1 == o2_bit] or o2_l

    for i in range(n_bit):
        co2_bit = sum((_l >> (n_bit - i)) & 1 for _l in co2_l) < len(co2_l) / 2
        co2_l = [_l for _l in co2_l if (_l >> (n_bit - i)) & 1 == co2_bit] or co2_l

    return o2_l[0] * co2_l[0]


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = [int(x, 2) for x in file]
        n_bit = max(bit.bit_length() for bit in data)

    print(solution1(data, n_bit))
    print(solution2(data, n_bit))
