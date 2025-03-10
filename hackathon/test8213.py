
def generate_subsets(array):
    subsets = []
    length = len(array)
    for mask in range(1 << length):
        subset = []
        for i in range(length):
            if mask & (1 << i):
                subset.append(array[i])
        subsets.append(subset)
    return subsets


def can_divide_equally(subset, target):
    length = len(subset)
    dp = [False] * (target + 1)
    dp[0] = True
    for weight in subset:
        for j in range(target, weight - 1, -1):
            dp[j] = dp[j] or dp[j - weight]
    return dp[target]


def find_possible_weights(weights):
    possible_sums = set()
    subsets = generate_subsets(weights)
    for subset in subsets:
        total = sum(subset)
        if total % 2 == 0:
            half = total // 2
            if can_divide_equally(subset, half):
                possible_sums.add(total)
    return possible_sums


n, m = map(int, input().split())
bars = list(map(int, input().split()))
weights = list(map(int, input().split()))


possible_weights = set()
for bar in bars:
    pancake_weights = find_possible_weights(weights)
    for w in pancake_weights:
        possible_weights.add(bar + w)


for weight in sorted(possible_weights):
    print(weight)