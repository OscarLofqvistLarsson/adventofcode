def part1():
    with open ("2025/inputday2.txt", "r") as input:

        invalid = 0

        for line in input:
            lst = line.split(",")
            parsed = [int(n) for _ in lst for n in _.split("-")]

        while len(parsed) >= 2:
            start, end = parsed[0], parsed[1]
            for j in range(start , end + 1):
                if str(j)[len(str(j))//2:] == str(j)[:len(str(j))//2]:
                    invalid += j
            parsed = parsed[2:]
        print(invalid)

def reppat(n):
    s = str(n)
    for size in range(1, len(s) // 2 + 2):
        if len(s) % size == 0:
            part = s[:size]
            repc = len(s) // size
            if repc > 1 and part * (len(s) // size) == s:
                return True
    return False

def part2():
    with open ("2025/inputday2.txt", "r") as input:

        invalid = 0

        for line in input:
            lst = line.split(",")
            parsed = [int(n) for _ in lst for n in _.split("-")]

        while len(parsed) >= 2:
            start, end = parsed[0], parsed[1]
            for j in range(start , end + 1):
                if reppat(j) or str(j)[len(str(j))//2:] == str(j)[:len(str(j))//2]:
                    invalid += j
            parsed = parsed[2:]
        print(invalid)



if __name__ == "__main__":
    part1()
    part2()