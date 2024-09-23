n=int(input())
restaurants=[]  

for i in range(n):
    city, score=input().split()
    score=int(score)
    restaurants.append((city, score, i+1))

restaurants.sort(key=lambda x: (x[0], -x[1]))

for restaurant in restaurants:
    print(restaurant[2])