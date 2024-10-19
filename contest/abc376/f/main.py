import sys

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

N, Q = map(int, input().split())
commands = []
for _ in range(Q):
    Hi_Ti = input().strip().split()
    Hi, Ti = Hi_Ti[0], int(Hi_Ti[1])
    commands.append((Hi, Ti))

lpos = 1
rpos = 2
total_moves = 0

for Hi, Ti in commands:
    if Hi == 'L':
        move_hand = 'L'
        move_pos = lpos
        other_pos = rpos
    else:
        move_hand = 'R'
        move_pos = rpos
        other_pos = lpos

    min_total = None
    for direction in ['cw', 'ccw']:
        if direction == 'cw':
            distance = (Ti - move_pos) % N
            path = [(move_pos + i - 1) % N + 1 for i in range(1, distance + 1)]
        else:
            distance = (move_pos - Ti) % N
            path = [(move_pos - i - 1) % N + 1 for i in range(1, distance + 1)]
        other_moves = 0
        other_current_pos = other_pos
        other_moved = False
        path_set = set(path)
        if other_current_pos in path_set:
            while other_current_pos in path_set:
                candidates = [((other_current_pos + 1 - 1) % N + 1),
                              ((other_current_pos - 1 - 1) % N + 1)]
                candidates = [pos for pos in candidates if pos != move_pos]
                moved = False
                for pos in candidates:
                    if pos not in path_set:
                        other_current_pos = pos
                        other_moves += 1
                        moved = True
                        break
                if not moved:
                    other_current_pos = candidates[0]
                    other_moves += 1
                other_moved = True
        total = distance + other_moves
        if min_total is None or total < min_total:
            min_total = total
            best_direction = direction
            best_other_moves = other_moves
            best_other_current_pos = other_current_pos

    if move_hand == 'L':
        if best_direction == 'cw':
            lpos = (lpos + (Ti - lpos) % N) % N
            if lpos == 0:
                lpos = N
        else:
            lpos = (lpos - (lpos - Ti) % N) % N
            if lpos == 0:
                lpos = N
        rpos = best_other_current_pos
    else:
        if best_direction == 'cw':
            rpos = (rpos + (Ti - rpos) % N) % N
            if rpos == 0:
                rpos = N
        else:
            rpos = (rpos - (rpos - Ti) % N) % N
            if rpos == 0:
                rpos = N
        lpos = best_other_current_pos

    total_moves += min_total

print(total_moves)
