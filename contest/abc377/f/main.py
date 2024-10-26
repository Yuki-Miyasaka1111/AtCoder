import sys

data = sys.stdin.read().split()
idx = 0

N = int(data[idx]); idx +=1
M = int(data[idx]); idx +=1

R = set()
C = set()
MD = set()
AD = set()

for _ in range(M):
    a = int(data[idx]); idx +=1
    b = int(data[idx]); idx +=1
    R.add(a)
    C.add(b)
    d_main = a - b
    d_anti = a + b
    MD.add(d_main)
    AD.add(d_anti)

# 1: |R| * N
Term1 = len(R) * N

# 2: |C| * N
Term2 = len(C) * N

# 3: sum(N - |d| for d in MD)
Term3 = 0
for d in MD:
    Term3 += N - abs(d)

# 4: sum(N - |d - (N + 1)| for d in AD)
Term4 = 0
for d in AD:
    Term4 += N - abs(d - (N +1))

# 5: |R| * |C|
Term5 = len(R) * len(C)

# 6: |A ∩ C|
count_A_C =0
for r in R:
    for d in MD:
        j = r - d
        if 1 <= j <= N:
            count_A_C +=1

# 7: |A ∩ D|
count_A_D =0
for r in R:
    for d in AD:
        j = d - r
        if 1 <= j <= N:
            count_A_D +=1

# 8: |B ∩ C|
count_B_C =0
for c in C:
    for d in MD:
        i = d + c
        if 1 <= i <= N:
            count_B_C +=1

# 9: |B ∩ D|
count_B_D =0
for c in C:
    for d in AD:
        i = d - c
        if 1 <= i <= N:
            count_B_D +=1

# 10: |C ∩ D|
count_C_D =0
for d1 in MD:
    for d2 in AD:
        if (d1 + d2) % 2 !=0:
            continue
        i = (d1 + d2) // 2
        j = (d2 - d1) // 2
        if 1 <= i <= N and 1 <= j <= N:
            count_C_D +=1

# 11: |A ∩ B ∩ C|
count_A_B_C =0
for r in R:
    for c in C:
        d = r - c
        if d in MD:
            count_A_B_C +=1

# 12: |A ∩ B ∩ D|
count_A_B_D =0
for r in R:
    for c in C:
        d = r + c
        if d in AD:
            count_A_B_D +=1

# 13: |A ∩ C ∩ D|
count_A_C_D =0
for r in R:
    for d1 in MD:
        d2 = 2 * r - d1
        if d2 in AD and (d2 - d1) %2 ==0:
            c = (d2 - d1) // 2
            if 1 <= c <= N:
                count_A_C_D +=1

# 14: |B ∩ C ∩ D|
count_B_C_D =0
for c in C:
    for d1 in MD:
        d2 = d1 + 2 * c
        if d2 in AD:
            i = d1 + c
            if 1 <= i <= N:
                count_B_C_D +=1

# 15: |A ∩ B ∩ C ∩ D|
count_A_B_C_D =0
for r in R:
    for c in C:
        d1 = r - c
        d2 = r + c
        if d1 in MD and d2 in AD:
            count_A_B_C_D +=1

cells_under_attack = Term1 + Term2 + Term3 + Term4 \
                    - Term5 - count_A_C - count_A_D - count_B_C - count_B_D - count_C_D \
                    + count_A_B_C + count_A_B_D + count_A_C_D + count_B_C_D \
                    - count_A_B_C_D

result = N * N - cells_under_attack

print(result)