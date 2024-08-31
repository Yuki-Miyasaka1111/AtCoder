x1,y1=map(int, input().split())
x2,y2=map(int, input().split())
x3,y3=map(int, input().split())

X = [elem for elem in [x1,x2,x3] if [x1,x2,x3].count(elem) == 1]
Y = [elem for elem in [y1,y2,y3] if [y1,y2,y3].count(elem) == 1]

print(" ".join(map(str, X + Y)))