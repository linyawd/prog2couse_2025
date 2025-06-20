n = int(input())
a = list(map(int, input().split()))
min_a = min(a)
max_a = max(a)
cnt = [0] * (max_a - min_a + 1)
for x in a:
    cnt[x - min_a] += 1
res = []
for i, c in enumerate(cnt):
    res.extend([i + min_a] * c)
print(' '.join(map(str, res)))
