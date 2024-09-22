n=int(input())
a=list(map(int,input().split()))

min_cost = 10 ** 18

for target in range(-100, 101):
    curret_cost = 0
    for num in a:
        curret_cost += (num - target) ** 2

    min_cost = min(min_cost, curret_cost)

print(min_cost)