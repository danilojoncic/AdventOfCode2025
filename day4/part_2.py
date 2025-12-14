def check_cell(row:int,col:int,matrix) -> bool:
    if matrix[row][col] != '@': return False
    counter = 0

    rows = len(matrix)
    cols = len(matrix[0])

    if row + 1 < rows and matrix[row + 1][col] == '@': counter += 1
    if row - 1 >= 0 and matrix[row - 1][col] == '@': counter += 1
    if col + 1 < cols and matrix[row][col + 1] == '@': counter += 1
    if col - 1 >= 0 and matrix[row][col - 1] == '@': counter += 1
    if row + 1 < rows and col + 1 < cols and matrix[row + 1][col + 1] == '@': counter += 1
    if row + 1 < rows and col - 1 >= 0 and matrix[row + 1][col - 1] == '@': counter += 1
    if row - 1 >= 0 and col + 1 < cols and matrix[row - 1][col + 1] == '@': counter += 1
    if row - 1 >= 0 and col - 1 >= 0 and matrix[row - 1][col - 1] == '@': counter += 1

    return counter < 4


def solve()-> int:

    matrix = []
    with open('/path/to/input.txt', 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))

    total_removed = 0
    while True:
        to_be_removed = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if check_cell(row, col, matrix):
                    to_be_removed.append((row, col))

        if len(to_be_removed) == 0:
            break

        for row, col in to_be_removed:
            matrix[row][col] = '.'

        total_removed += len(to_be_removed)

    return total_removed



if __name__ == '__main__':
    result = solve()
    print(result)