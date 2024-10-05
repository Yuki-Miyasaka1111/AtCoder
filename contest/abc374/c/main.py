n=int(input())
k=list(map(int,input().split()))

total_sum = sum(k)
min_max_group_sum = float('inf')

for i in range(1 << n):
    gA = 0
    gB = 0

    for j in range(n):
        if i & (1 << j):
            gA += k[j]
        else:
            gB += k[j]

    max_group_sum = max(gA, gB)
    min_max_group_sum = min(min_max_group_sum, max_group_sum)

print(min_max_group_sum)