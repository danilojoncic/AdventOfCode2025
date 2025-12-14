def one_pass(line: str, k: int) -> int:
    #using a monotonic stack to create a 12 digit number where
    #next number is less than or equal to current number
    stack = []

    length = len(line)
    for i, ch in enumerate(line):
        digit = int(ch)
        while stack and digit > stack[-1] and len(stack) + (length - i) > k:
            stack.pop()
        if len(stack) < k:
            stack.append(digit)

    return int("".join(map(str, stack)))

def solve_one_pass() -> int:
    total = 0
    k = 12

    with open('/path/to/intput.txt', 'r') as file:
        for line in file:
            line = line.strip()
            total += one_pass(line,k)

    return total


if __name__ == '__main__':
    result = solve_one_pass()
    print(result)