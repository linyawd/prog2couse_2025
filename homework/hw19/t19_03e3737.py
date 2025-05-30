n = int(input())
a = list(map(int, input().split()))
a = [0] + a
ok = True
for i in range(1, n + 1):
    if 2 * i <= n and a[i] > a[2 * i]:
        ok = False
    if 2 * i + 1 <= n and a[i] > a[2 * i + 1]:
        ok = False
print("YES" if ok else "NO")
