from collections import deque

n = int(input())
p1 = deque(map(int, input().split()))
p2 = deque(map(int, input().split()))

max_turns = 200000
turns = 0

while p1 and p2 and turns < max_turns:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if (c1 > c2 and not (c2 == 0 and c1 == n-1)) or (c1 == 0 and c2 == n-1):
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c1)
        p2.append(c2)
    turns += 1

if turns == max_turns:
    print("draw")
else:
    if p1:
        print("first", turns)
    else:
        print("second", turns)