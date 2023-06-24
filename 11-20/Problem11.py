def find_number(list, x, y):
    return list[y - 1][x - 1]

def maximise_vertical(list):
    highest = 0
    record = 1
    for j in range(1, 20 + 1):
        for i in range(1, 17):
            record = 1
            for k in range(0, 4):
                record = record * find_number(list, j, i + k)
            if record > highest:
                highest = record
    return highest

def maximise_horizontal(list):
    highest = 0
    record = 0
    for j in range(1, 20 + 1):
        for i in range(1, 17):
            record = 1
            for k in range(0, 4):
                record = record * find_number(list, i + k, j)
            if record > highest:
                highest = record
    return highest

def maximise_diagonal(list):
    highest = 0
    record = 0
    for i in range(1, 20 - 4 + 1):
        for j in range(1, 20 - 4 + 1):
            record = 1
            for k in range(0, 4):
                record = record * find_number(list, i + k, j + k)
            if record > highest:
                highest = record
    for i in range(20 - 4, 1 + 1, -1):
        for j in range(1, 20 - 4 + 1):
            record = 1
            for k in range(0, 4):
                record = record * find_number(list, i - k, j + k)
            if record > highest:
                highest = record
    for i in range(1, 20 - 4 + 1):
        for j in range(20 - 4, 1 + 1, -1):
            record = 1
            for k in range(0, 4):
                record = record * find_number(list, i + k, j - k)
            if record > highest:
                highest = record
    for i in range(20 - 4, 1 + 1, -1):
        for j in range(20 - 4, 1 + 1, -1):
            record = 1
            for k in range(0, 4):
                record = record * find_number(list, i - k, j - k)
            if record > highest:
                highest = record
    return highest
    

if __name__ == '__main__':
    grid = []
    for i in range(0, 20):
        line = input()
        line = [int(num) for num in line.split()]
        grid.append(line)
    print(max(maximise_vertical(grid), maximise_diagonal(grid), maximise_horizontal(grid)))