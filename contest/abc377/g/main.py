import sys

data = sys.stdin.read().split()
idx = 0

N = int(data[idx]); idx += 1

S = []
for _ in range(N):
    S.append(data[idx])
    idx +=1

children = [[-1]*26]
min_length = [float('inf')]

for k in range(1, N+1):
    Sk = S[k-1]
    len_Sk = len(Sk)
    min_cost = len_Sk

    current_node = 0
    l = 0
    possible_costs = []

    while l < len_Sk:
        c = Sk[l]
        c_idx = ord(c) - ord('a')

        if children[current_node][c_idx] == -1:
            break

        current_node = children[current_node][c_idx]
        l +=1

        current_min_length = min_length[current_node]
        if current_min_length != float('inf'):
            cost = len_Sk + current_min_length - 2*l
            possible_costs.append(cost)

    if possible_costs:
        min_cost = min(min_cost, min(possible_costs))

    print(min_cost)

    current_node =0
    for c in Sk:
        c_idx = ord(c) - ord('a')
        if children[current_node][c_idx] == -1:
            children[current_node][c_idx] = len(children)
            children.append([-1]*26)
            min_length.append(float('inf'))
        current_node = children[current_node][c_idx]
        if len_Sk < min_length[current_node]:
            min_length[current_node] = len_Sk