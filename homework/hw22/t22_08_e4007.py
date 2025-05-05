from collections import deque


def neighbors(s):
    res = []
    digits = list(s)

    if digits[0] != '9':
        new_digits = digits[:]
        new_digits[0] = str(int(new_digits[0]) + 1)
        res.append(''.join(new_digits))

    if digits[3] != '1':
        new_digits = digits[:]
        new_digits[3] = str(int(new_digits[3]) - 1)
        res.append(''.join(new_digits))

    res.append(digits[-1] + ''.join(digits[:-1]))
    res.append(''.join(digits[1:]) + digits[0])

    return [x for x in res if '0' not in x]


a = input().strip()
b = input().strip()

q = deque([a])
prev = {a: None}

while q:
    u = q.popleft()
    if u == b:
        break
    for v in neighbors(u):
        if v not in prev:
            prev[v] = u
            q.append(v)

path = []
while b:
    path.append(b)
    b = prev[b]

print('\n'.join(reversed(path)))
