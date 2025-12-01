def part1():

    dial = list(range(100))
    current = 50
    points = 0

    with open("2025/inputday1.txt", "r") as input:

        lines = input.readlines()
        for line in lines:
            if line[0] == "R":
                current += int(line[1:])
                current = dial[current % 100]
                if current == 0:
                    points += 1
            else:
                current -= int(line[1:])
                current = dial[current % 100]
                if current == 0:
                    points += 1
    print(points)

def part2():
    current = 50
    points = 0

    with open("2025/inputday1.txt", "r") as input:

        lines = input.readlines()
        for line in lines:
            dir = line[0]
            steps = int(line[1:])
            old = current

            if dir == "R":
                current = (old + steps)
                rotations = current // 100
                points += rotations

                if old > 0 >= current:
                    points += 1

                current = current % 100

            else:
                current = (old - steps)
                rotations = abs(current) // 100
                points += rotations

                if old > 0 >= current:
                    points += 1

                current = current % 100

    print(points)

if __name__ == "__main__":
    part1()
    part2()