import os

# Simple lookup table for len(segments): digit
signal_len_lookup = {2: 1, 3: 7, 4: 4, 7: 8}


def decode_unknwon_signals(decoded_signals, unknown_signals):
    for unknown_signal in unknown_signals:
        leftover_wire = decoded_signals[8].difference(unknown_signal)
        if len(leftover_wire) == 1:
            if leftover_wire.issubset(decoded_signals[1]):
                decoded_signals[6] = unknown_signal
            elif leftover_wire.issubset(decoded_signals[4]):
                decoded_signals[0] = unknown_signal
            else:
                decoded_signals[9] = unknown_signal
        elif len(leftover_wire) == 2:
            if leftover_wire.issubset(decoded_signals[4]):
                decoded_signals[2] = unknown_signal
            elif leftover_wire.issubset(
                decoded_signals[8].difference(decoded_signals[1])
            ):
                decoded_signals[3] = unknown_signal
            else:
                decoded_signals[5] = unknown_signal
    return decoded_signals


def solution1(notes):
    t = 0
    for _, output_signals in notes:
        t += sum(len(signal) in signal_len_lookup.keys() for signal in output_signals)
    return t


def solution2(notes):
    digits = []
    get_digits = lambda signal, decoded_signals: str(
        list(decoded_signals.keys())[list(decoded_signals.values()).index(signal)]
    )
    for unique_signals, output_signals in notes:
        unknown_signals = list()
        decoded_signals = {i: set() for i in range(10)}
        for signal in unique_signals:
            if len(signal) in signal_len_lookup.keys():
                decoded_signals[signal_len_lookup[len(signal)]] = signal
            else:
                if signal not in unknown_signals:
                    unknown_signals.append(signal)
        decoded_signals = decode_unknwon_signals(decoded_signals, unknown_signals)
        digits.append(
            "".join(
                [
                    get_digits(output_signal, decoded_signals)
                    for output_signal in output_signals
                ]
            )
        )
    return sum(map(int, digits))


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    get_notes = lambda notes: [list(map(set, signal.split())) for signal in notes]
    signals_notes = [get_notes(note.split("|")) for note in data]

    print(solution1(signals_notes))
    print(solution2(signals_notes))
