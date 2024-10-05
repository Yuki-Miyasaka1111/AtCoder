s = input()
t = input()

if s == t:
    print("0")
else:
    found_difference = False

    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            print(i + 1)
            found_difference = True
            break

    if not found_difference:
        print(min(len(s), len(t)) + 1)