def day_two_part_one():
    with open("day2.txt") as f:
        games = [i.strip() for i in f.readlines()]

    total = 0

    for game in games:
        game, inp = game.split(":")
        id = int("".join([l for l in game if l.isdigit()]))
        rounds = inp.split(";")
        rounds = [r.strip() for r in rounds]
        rounds = [r.split(",") for r in rounds]
        possibles = []

        for cubes in rounds:
            for c in cubes:
                c = c.strip()
                no_of_c = int("".join([l for l in c if l.isdigit()]))
                if "green" in c:
                    if no_of_c > 13:
                        possibles.append(False)
                        break
                elif "blue" in c:
                    if no_of_c > 14:
                        possibles.append(False)
                        break
                elif "red" in c:
                    if no_of_c > 12:
                        possibles.append(False)
                        break

            else:
                possibles.append(True)

        if False not in possibles:
            total += id

    return total


def day_two_part_two():
    with open("day2.txt") as f:
        games = [i.strip() for i in f.readlines()]

    total = 0

    for game in games:
        game, inp = game.split(":")
        rounds = inp.split(";")
        rounds = [r.strip() for r in rounds]
        rounds = [r.split(",") for r in rounds]

        scores = []

        for cubes in rounds:
            round_score = {"red": 0, "green": 0, "blue": 0}
            for c in cubes:
                c = c.strip()
                no_of_c = int("".join([l for l in c if l.isdigit()]))
                if "green" in c:
                    round_score["green"] = no_of_c
                elif "blue" in c:
                    round_score["blue"] = no_of_c
                elif "red" in c:
                    round_score["red"] = no_of_c

            scores.append(round_score)

        max_red = max(color["red"] for color in scores)
        max_green = max(color["green"] for color in scores)
        max_blue = max(color["blue"] for color in scores)

        total += max_red * max_green * max_blue

    return total
