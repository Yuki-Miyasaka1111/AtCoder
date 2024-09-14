# def S(n):
#     if n == 1:
#         return [1]
#     else:
#         return S(n-1) + [n] + S(n-1)
    
# n = int(input())
# print(*S(n))

memo = {}

def S(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return [1]
    else:
        ret = S(n - 1) + [n] + S(n - 1)
    memo[n] = ret
    return memo[n]

N = int(input())
print(*S(N))