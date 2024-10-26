# ナイトの動き
knight_moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

N, M = map(int, input().split())
pieces = [tuple(map(int, input().split())) for _ in range(M)]

piece_set = set((a, b) for a, b in pieces)
attack_set = set()

for a, b in pieces:
    for da, db in knight_moves:
        na, nb = a + da, b + db
        if 1 <= na <= N and 1 <= nb <= N and (na, nb) not in piece_set:
            attack_set.add((na, nb))

total_spaces = N * N
attacked_spaces = len(attack_set)
piece_count = len(piece_set)

safe_spaces = total_spaces - attacked_spaces - piece_count

print(safe_spaces)
