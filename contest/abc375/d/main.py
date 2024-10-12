S = input().strip()
N = len(S)

positions = {}
for idx, c in enumerate(S):
    if c not in positions:
        positions[c] = []
    positions[c].append(idx + 1)

total_triplets = 0

for c in positions:
    pos_list = positions[c]
    sum_positions = 0
    n = len(pos_list)
    for i in range(n):
        p_i = pos_list[i]
        if i >= 1:
            total_triplets += p_i * i - sum_positions - i
        sum_positions += p_i

print(total_triplets)
