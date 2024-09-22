s=input()

ans=[]
for char in s:
    if char == "0" or char == "1":
        ans.append(char)
    else:
        if len(ans) > 0:
            ans.pop()

print("".join(ans))