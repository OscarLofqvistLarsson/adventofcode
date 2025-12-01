def main():

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

if __name__ == "__main__":
    main()