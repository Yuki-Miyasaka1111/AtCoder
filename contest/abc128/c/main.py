N,M = map(int, input().split())

switches = []
p = []

for _ in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    switches.append(data[1:k+1])
p = list(map(int, input().split()))

count = 0
for bit in range(1 << N):
    all_on = True

    for i in range(M):
        on_count = 0
        for switch in switches[i]:
            if bit & (1 << (switch-1)):
                on_count += 1
        
        if on_count % 2 != p[i]:
            all_on = False
            break
    if all_on:
        count += 1

print(count)