import sys

def is_bst_path(path):
    def check(i, low, high):
        if i == len(path):
            return False
        x = path[i]
        if not (low < x < high):
            return False
        j = i + 1
        while j < len(path):
            if path[j] < x:
                break
            if path[j] > x:
                break
            j += 1
        if j == len(path):
            return True
        if path[j] < x:
            return check(j, low, x)
        return check(j, x, high)

    return "YES" if check(0, float("-inf"), float("inf")) else "NO"

data = sys.stdin.read()
numbers = list(map(int, data.strip().split()))
print(is_bst_path(numbers))
