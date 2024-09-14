n=int(input())
a=list(map(int,input().split()))
last_seen=[-1]*(n+1)
curr_total=0
res=0

for i in range(n):
    num_subarrays_ending_at_i=i+1
    if last_seen[a[i]]==-1:
        num_new = num_subarrays_ending_at_i
    else:
        num_new=i-last_seen[a[i]]
    curr_total+=num_new
    res+=curr_total
    last_seen[a[i]]=i
print(res)