s=input()
n=len(s)

total_sum=0

for bit in range(1 << (n - 1)):
    current_expression = ""
    for i in range(n):
        current_expression += s[i]
        if bit & (1<<i):
            current_expression += "+"
    total_sum += eval(current_expression)
print(total_sum)