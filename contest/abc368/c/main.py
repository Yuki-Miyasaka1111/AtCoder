N = int(input())
H = list(map(int, input().split()))

T = 0

for h in H:
    # 5ダメージごとに3ターンかかることを利用する
    if h > 5:
        full_cycles = h // 5  # 5ダメージごとに3ターンかかる
        T += full_cycles * 3
        h -= full_cycles * 5
    
    # 残りの体力が5未満の場合は1ずつ減らす
    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1

print(T)