N = int(input())
A=list(map(int, input().split()))

count = 0
length = 1

for i in range(1, N):
    if i == 1 or A[i] - A[i-1] == A[i-1] - A[i-2]:
        length += 1
    else:
        count += (length - 1) * length // 2
        length = 2

# 最後の部分列もカウント
count += (length - 1) * length // 2

# 全ての要素単体の部分列を加算（長さ1の部分列）
count += N

print(count)