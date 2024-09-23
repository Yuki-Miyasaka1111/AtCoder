# ビット全探索の基本形
N = 3  # 探索する項目の数（例として3つの項目を扱う）
elements = [1, 2, 3]  # 探索対象の要素（例として数値1, 2, 3）

# 2^N 通りの状態をビット全探索
# 1 << N は 2^N を意味し、全てのビット状態を試すループ
for bit in range(1 << N):
    selected_elements = []  # 現在の状態で選ばれた要素を格納するリスト
    print(f"bit: {bit:0{N}b}")  # 現在のビット状態を2進数で表示（デバッグ用）
    
    for i in range(N):
        # ビット `bit` の i 番目が 1 かどうかをチェック
        # 1 << i は、i 番目のビットが 1 かどうかを確認するためのマスク
        if bit & (1 << i):
            selected_elements.append(elements[i])  # i 番目の要素を選択する

    # 現在のビット状態で選ばれた要素の表示
    print(f"選択された要素: {selected_elements}")

# ビット全探索の応用形
# 状態に応じた条件を満たすかチェックする
# (例: 選ばれた要素の和が特定の値になるかどうか)
target_sum = 5  # 目標の合計値
count = 0  # 条件を満たす組み合わせの数をカウント

for bit in range(1 << N):
    selected_sum = 0  # 選ばれた要素の合計
    for i in range(N):
        if bit & (1 << i):
            selected_sum += elements[i]  # i 番目の要素を合計に加える
    
    # 条件を満たすか確認
    if selected_sum == target_sum:
        count += 1  # 条件を満たす組み合わせのカウントを増やす
        print(f"条件を満たす組み合わせ: {bit:0{N}b}, 合計: {selected_sum}")

print(f"条件を満たす組み合わせの数: {count}")
