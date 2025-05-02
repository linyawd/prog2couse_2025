def main():
    with open("input.txt") as f:
        n = int(f.readline())
        adj = [[] for _ in range(n)]

        for i in range(n):
            row = list(map(int, f.readline().split()))
            for j in range(i + 1, n):
                if row[j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                count += 1
                stack = [i]
                visited[i] = True

                while stack:
                    current = stack.pop()
                    for neighbor in adj[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

        print(count)


if __name__ == "__main__":
    main()