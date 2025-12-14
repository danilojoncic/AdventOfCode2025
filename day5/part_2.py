def solve() -> int:
    ranges = []
    with open('path/to/input.txt') as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            parts = line.split('-')
            ranges.append((int(parts[0]), int(parts[1])))

    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    total = sum(end - start + 1 for start, end in merged)
    return total



if __name__ == '__main__':
    result = solve()
    print(result)