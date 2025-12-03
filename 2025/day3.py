def part1():
    with open("2025/inputday3.txt") as input:
        res = 0
        for line in input:
            line = str(line.strip())
            big,index = 0,0
            for i in line:
                index += 1
                if int(i) > int(big) and index < len(line):
                    big = i
                    indexbig = index

            ndbig = 0
            for i in line[indexbig:]:
                if int(i) > int(ndbig):
                    ndbig = i
            bigcomb = big + ndbig

            res += int(bigcomb)
        print(res)

def part2():
    with open("2025/inputday3.txt") as input:
        res = 0
        for line in input:
            line = str(line.strip())
            big,index, biggest = 0,0,""
            while len(biggest) < 12:
                for i in line:
                    index += 1
                    if int(i) > int(big) and index < (len(line) - (10 - len(biggest))):
                        big = i
                        indexbig = index
                biggest += str(big)
                big,index = 0,0
                line = line[indexbig:]

            res += int(biggest)
        print(res)


if __name__ == "__main__":
    part1()
    part2()