stack = []
top = -1

while True:
    cmd = input().split()
    if cmd[0] == 'push':
        n = int(cmd[1])
        top += 1
        if top < len(stack):
            stack[top] = n
        else:
            stack += [n]
        print('ok')
    elif cmd[0] == 'pop':
        if top >= 0:
            print(stack[top])
            top -= 1
        else:
            print('error')
    elif cmd[0] == 'back':
        if top >= 0:
            print(stack[top])
        else:
            print('error')
    elif cmd[0] == 'size':
        print(top + 1)
    elif cmd[0] == 'clear':
        top = -1
        print('ok')
    elif cmd[0] == 'exit':
        print('bye')
        break