FILE_PATH = 'path/to/input.txt'


def solve() -> int:
    result = 0
    numbers = []
    operations = []

    with open(FILE_PATH) as f:
        for index, line in enumerate(f):
            parts = line.strip().split()
            if index < 4:
                row = []
                for value in parts:
                    row.append(int(value))
                numbers.append(row)
            else:
                operations = parts
    for i in range(len(operations)):
        if operations[i] == '+':
            result += (
                numbers[0][i]
                + numbers[1][i]
                + numbers[2][i]
                + numbers[3][i]
            )
        elif operations[i] == '*':
            result += (
                numbers[0][i]
                * numbers[1][i]
                * numbers[2][i]
                * numbers[3][i]
            )
    return result

if __name__ == '__main__':
    print(solve())