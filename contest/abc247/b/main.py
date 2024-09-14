n=int(input())
s,t=[],[]

for i in range(n):
    u,v=map(str, input().split())
    s.append(u)
    t.append(v)

for i in range(n):
    nickname = False
    for S in [s[i], t[i]]:
        s_ok = True
        for j in range(n):
            if i != j:
                if S == s[j] or S == t[j]:
                    s_ok = False
        if s_ok:
            nickname = True
    if nickname == False:
        print("No")
        exit()

print("Yes")