from collections import deque

# クエリの数を取得
n = int(input())

# dequeを使ってボールの情報をランレングス符号化で管理
tube = deque()

# 出力結果を保持するリスト
results = []

# クエリの処理
for _ in range(n):
    query = input().split()
    
    if query[0] == "1":
        # 1 x c クエリ: xが書かれたボールをc個右側から入れる
        x = int(query[1])
        c = int(query[2])
        
        # tubeの右端に追加
        if tube and tube[-1][0] == x:
            tube[-1] = (x, tube[-1][1] + c)
        else:
            tube.append((x, c))
    
    elif query[0] == "2":
        # 2 c クエリ: 左側からc個取り出し、その合計を出力する
        c = int(query[1])
        sum_removed = 0
        
        while c > 0:
            num, count = tube[0]
            
            if count <= c:
                sum_removed += num * count
                c -= count
                tube.popleft()  # 全て取り出したので削除
            else:
                sum_removed += num * c
                tube[0] = (num, count - c)  # 取り出した分だけ減らす
                c = 0
        
        results.append(sum_removed)

# 結果を一度に出力
print("\n".join(map(str, results)))