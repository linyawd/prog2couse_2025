import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)

total_cost = 0
while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    cost = x + y
    total_cost += cost
    heapq.heappush(a, cost)

print(total_cost)
