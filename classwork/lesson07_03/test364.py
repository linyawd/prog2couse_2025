from math import factorial

def get_tarabarsky_word(N, k):
    letters = [chr(ord('a') + i) for i in range(N)]
    result = []
    k -= 1
    for i in range(N, 0, -1):
        fact = factorial(i - 1)
        index = k // fact
        result.append(letters.pop(index))
        k %= fact
    return ''.join(result)

N, k = map(int, input().split())
print(get_tarabarsky_word(N, k))