def check(grid, y, x):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for dx in (-1, 0 , 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue

            ny = y + dy
            nx = x + dx

            if 0 <= ny < rows and 0 <= nx < cols:
                if grid[ny][nx] == "@":
                    count += 1

    return count

def part1():
    with open("2025/inputday4.txt") as input:
        res = 0
        grid = [list(line.strip()) for line in input]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                    if grid[y][x] == "@":
                        if check(grid, y, x) < 4:
                            res += 1
                        #line = line[:index] + "." + line[index + 1:]
    print(res)

def part2():
    with open("2025/ex.txt") as input:
        grid = [list(line.strip()) for line in input]
        print(grid[1][0])
    return

if __name__ == "__main__":
    part1()
    part2()