max_result = 0


def find_max_sum(limit, numbers):
    global max_result
    max_result = 0
    total = sum(numbers)

    if total <= limit:
        return total

    if limit in numbers:
        return limit

    for i in range(len(numbers)):
        explore_combinations(numbers, numbers[i], i + 1, limit)

    return max_result


def explore_combinations(numbers, current_sum, index, limit):
    global max_result

    if current_sum > limit:
        return

    max_result = max(max_result, current_sum)

    if max_result == limit:
        return

    for i in range(index, len(numbers)):
        explore_combinations(numbers, current_sum + numbers[i], i + 1, limit)


if __name__ == "__main__":
    with open("input.txt") as file:
        for line in file:
            data = [int(x) for x in line.strip().split()]
            target, _ = data[0], data[1]
            elements = data[2:]
            outcome = find_max_sum(target, elements)
            print(f"sum:{outcome}")
