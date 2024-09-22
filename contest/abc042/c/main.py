n, k = map(int, input().split())
d = [int(i) for i in input().split()]

x = []
for i in range(10):
    if i not in d:
        x.append(i)

for i in range(n, 10**6):
    if all([digit in x for digit in map(int, str(i))]):
        print(i)
        break