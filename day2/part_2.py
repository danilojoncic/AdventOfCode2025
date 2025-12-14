
def isValid(id:int) -> bool:
    string = str(id)
    length = len(string)


    for substring_length in range(1,length // 2 + 1):
        #is not divisable
        if length % substring_length != 0 : continue

        substring = string[:substring_length]
        number = length // substring_length

        #multiply substring to create string made up of repeats
        if substring * number == string:
            return False

    return True






def solve() -> int:
    sum = 0;
    with open('path/to/input.txt', 'r') as file:
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