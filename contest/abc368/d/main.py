from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def solve():
    try:
        N, K = map(int, input().split())
        if K > N or N <= 0 or K <= 0:
            raise ValueError("不正な入力です。NとKの値を確認してください。")

        tree = defaultdict(list)

        for _ in range(N - 1):
            A, B = map(int, input().split())
            if A <= 0 or B <= 0 or A > N or B > N:
                raise ValueError("不正な頂点番号です。")
            tree[A].append(B)
            tree[B].append(A)

        V = set(map(int, input().split()))
        if len(V) != K or any(v <= 0 or v > N for v in V):
            raise ValueError("指定された重要な頂点が不正です。")

        def dfs(node, parent):
            size = 0
            found_important = (node in V)

            for neighbor in tree[node]:
                if neighbor != parent:
                    sub_size, sub_found_important = dfs(neighbor, node)
                    if sub_found_important:
                        size += sub_size
                        found_important = True

            if found_important:
                size += 1

            return size, found_important

        root = next(iter(V))
        result, _ = dfs(root, -1)
        
        print(result)
    
    except ValueError as ve:
        print(f"エラー: {ve}")
    except RecursionError:
        print("再帰の深さが上限を超えました。入力サイズが大きすぎます。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

# 実行
solve()
