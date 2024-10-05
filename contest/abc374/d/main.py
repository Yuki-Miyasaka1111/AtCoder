import sys
import math

# 入力の読み込み
N_str, S_str, T_str = sys.stdin.readline().split()
N = int(N_str)
S = float(S_str)
T = float(T_str)

segments = []
positions = [(0.0, 0.0)]  # 位置リスト[0] は (0,0)
pos_dict = { (0.0, 0.0): 0 }  # 座標をインデックスにマッピング

for i in range(N):
    A_i_str, B_i_str, C_i_str, D_i_str = sys.stdin.readline().split()
    A_i, B_i, C_i, D_i = map(float, (A_i_str, B_i_str, C_i_str, D_i_str))
    segments.append(((A_i, B_i), (C_i, D_i)))
    if (A_i, B_i) not in pos_dict:
        pos_dict[(A_i, B_i)] = len(positions)
        positions.append((A_i, B_i))
    if (C_i, D_i) not in pos_dict:
        pos_dict[(C_i, D_i)] = len(positions)
        positions.append((C_i, D_i))

position_count = len(positions)
dp_size = 1 << N
dp = [ [math.inf] * position_count for _ in range(dp_size) ]
dp[0][0] = 0.0  # (0,0)から開始、何も印字していない状態

for printed_segments in range(dp_size):
    for current_position in range(position_count):
        current_time = dp[printed_segments][current_position]
        if current_time == math.inf:
            continue
        current_x, current_y = positions[current_position]
        # 未印字の線分について
        for i in range(N):
            if not (printed_segments & (1 << i)):
                # 始点として両方の端点を試す
                for start_point in [0, 1]:
                    start = segments[i][start_point]
                    end = segments[i][1 - start_point]
                    start_index = pos_dict[start]
                    end_index = pos_dict[end]
                    # 現在位置から始点までの移動時間（レーザ非照射時）
                    dx_move = positions[start_index][0] - current_x
                    dy_move = positions[start_index][1] - current_y
                    distance_move = math.hypot(dx_move, dy_move)
                    time_move = distance_move / S
                    # 始点から終点までの印字時間（レーザ照射時）
                    dx_print = positions[end_index][0] - positions[start_index][0]
                    dy_print = positions[end_index][1] - positions[start_index][1]
                    distance_print = math.hypot(dx_print, dy_print)
                    time_print = distance_print / T
                    total_time = current_time + time_move + time_print
                    next_printed_segments = printed_segments | (1 << i)
                    # dpの更新
                    if dp[next_printed_segments][end_index] > total_time:
                        dp[next_printed_segments][end_index] = total_time

min_time = math.inf
full_printed_set = (1 << N) - 1
for p in range(position_count):
    if dp[full_printed_set][p] < min_time:
        min_time = dp[full_printed_set][p]

# 精度を十分に確保して出力
print("%.20f" % min_time)
