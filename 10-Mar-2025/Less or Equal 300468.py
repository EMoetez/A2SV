# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if k == 0:  
    print(a[0] - 1 if a[0] > 1 else -1)
elif k < n and a[k] == a[k - 1]: 
    print(-1)
else:
    print(a[k - 1])  
