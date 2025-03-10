def generate_permutations(n, k):
    def backtrack(start, path):
        if len(path) == k:
            print(' '.join(map(str, path)))
            return
        for i in range(1, n + 1):
            if i not in path:
                backtrack(start + 1, path + [i])

    backtrack(0, [])

n, k = map(int, input().split())
generate_permutations(n, k)