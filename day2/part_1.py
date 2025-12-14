
def isValid(id:int) -> bool:
    string = str(id)
    if(len(string) % 2 != 0) : return True

    half = int(len(string) / 2)
    first = string[:half]
    last = string[half:]

    return first != last


def solve() -> int:
    sum = 0;
    with open('/path/to/input.txt', 'r') as file:
        line = file.readline().strip()
        ranges = line.split(',')

        for rng in ranges:

            parts = rng.split('-')
            left = int(parts[0])
            right = int(parts[1])

            for val in range(left,right + 1):
                if not isValid(val):
                    sum += val

    return sum





if __name__ == '__main__':
    result = solve()
    print(result)