def part1():

    with open("2025/inputday5.txt") as input:
        ranges = []
        IDs = set()
        for line in input:
            line = line.strip()
            if "-" in line:
                ranges.append(tuple(map(int, line.split("-"))))
            if "-" not in line:
                if line == "":
                    continue
                else:
                    IDs.add(int(line))

        fresh = set()
        for start, end in ranges:
            for i in IDs:
                if start < i < end:
                    fresh.add(i)

        print(f"Amount of fresh ingrediens {len(fresh)} \n")


def part2():
    return


if __name__ == "__main__":
    part1()
    part2()
