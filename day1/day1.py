def day_one_part_one():
    with open("day1.txt") as f:
        arr = [i.strip() for i in f.readlines()]

    total = 0
    for l in arr:
        parsed_line = [i for i in l if i.isdigit()]
        val = int(str(parsed_line[0]) + str(parsed_line[-1]))
        total += val

    return total


def day_one_part_two():
    hashmap = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    with open("day1.txt") as f:
        arr = [i.strip() for i in f.readlines()]

    total = 0

    for line in arr:
        idx_to_digit = {}
        for idx, letter in enumerate(line):
            if letter.isdigit():
                idx_to_digit[idx] = str(letter)

        for word, digit in hashmap.items():
            start = 0
            while True:
                start = line.find(word, start)
                if start == -1:
                    break
                idx_to_digit[start] = digit
                start += len(word)

        lowest, highest = (
            idx_to_digit[min(idx_to_digit)],
            idx_to_digit[max(idx_to_digit)],
        )
        total += int(lowest + highest)

    return total
