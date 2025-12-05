def part1():

    with open("2025/ex.txt") as input:
        ranges = []
        IDs = set()
        for line in input:
            if "-" in line:
                ranges.append(line.strip())
            if "-" not in line:
                if line == "\n":
                    continue
                else:
                    IDs.add(int(line.strip()))

        fresh = 0
        counted = set()
        for r in ranges:
            start, end = map(int, r.split("-"))
            for i in range(start, end + 1):
                if i in IDs and i not in counted:
                    fresh += 1
                    counted.add(i)


        print(f"Amount of fresh ingrediens {fresh} \n")


def part2():
    return


if __name__ == "__main__":
    part1()
    part2()
