def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        while True:
            line = input().strip()
            if line == '0':
                print()
                break
            target = list(map(int, line.split()))
            stack = [0] * 1001
            top = -1
            current = 1
            possible = True
            for wagon in target:
                while current <= n and (top == -1 or stack[top] != wagon):
                    top += 1
                    stack[top] = current
                    current += 1
                if top >= 0 and stack[top] == wagon:
                    top -= 1
                else:
                    possible = False
                    break
            print('Yes' if possible else 'No')

solve()