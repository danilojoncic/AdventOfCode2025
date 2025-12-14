#we can do this by brute force O(N2) or by one pass O(N)
def solve()-> int:
    sum = 0
    with open('/path/to/intput.txt', 'r') as file:
        for f in file:
            row = f.strip()
            max_of_row = 0
            for i in range(len(row)-1):
                for j in range(i+1, len(row)):
                    calculation = int(row[i]) * 10 + int(row[j])
                    if calculation >= max_of_row:
                        max_of_row = calculation
            sum += max_of_row
    return sum

def one_pass(line: str) -> int:
    best_tens = -1
    best_value = -1

    for ch in line:
        digit = int(ch)

        if best_tens != -1:
            best_value = max(best_value, best_tens * 10 + digit)

        best_tens = max(best_tens, digit)

    return best_value

def solve_one_pass() -> int:
    total = 0

    with open('/path/to/intput.txt', 'r') as file:
        for line in file:
            line = line.strip()
            total += one_pass(line)

    return total


if __name__ == '__main__':
    result = solve_one_pass()
    print(result)