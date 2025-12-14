def solve()-> int:
    id_ranges = []
    range_bool = True
    fresh_number = 0
    with open('/path/to/input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                range_bool = False
                continue

            if range_bool:
                parts = line.split('-')
                id_ranges.append((int(parts[0]), int(parts[1])))
            else:
                id = int(line)
                for range in id_ranges:
                    if range[0] <= id <= range[1]:
                        fresh_number += 1
                        break;
    return fresh_number



if __name__ == '__main__':
    result = solve()
    print(result)