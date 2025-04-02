def find_partitions(n, max_val, current_partition, result):
    if n == 0:
        result.append("+".join(map(str, current_partition)))
        return

    for i in range(1, min(n, max_val) + 1):
        find_partitions(n - i, i, current_partition + [i], result)

def generate_partitions(n):
    result = []
    find_partitions(n, n - 1, [], result)
    return result


if __name__ == "__main__":
    N = int(input().strip())
    partitions = generate_partitions(N)
    for partition in partitions:
        print(partition)