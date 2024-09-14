n,m=map(int, input().split())

first_mail=[]
for _ in range(m):
    a, b = input().split()
    if a not in first_mail and b=="M":
        print("Yes")
        first_mail.append(a)
    else:
        print("No")
