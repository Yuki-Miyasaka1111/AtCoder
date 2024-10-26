row_has_piece = [False] * 8
col_has_piece = [False] * 8

board = [list(input().strip()) for _ in range(8)]

for i in range(8):
    for j in range(8):
        if board[i][j] == "#":
            row_has_piece[i] = True
            col_has_piece[j] = True

safe_cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == "." and not row_has_piece[i] and not col_has_piece[j]:
            safe_cnt += 1

print(safe_cnt)
