# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n=int(input())
order=[]
seen=set()
for i in range(n):
    order.append(input())
    
for i in range(n-1,-1,-1): 
    if order[i] not in seen:
        seen.add(order[i])
        print(order[i])
