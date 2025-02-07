# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s, n= list(map(int,input().split()))
dragons = []
for i in range(n):
    dragons.append(list(map(int,input().split())))
dragons.sort()
for i in range(n):
    if s>dragons[i][0]:
        s+=dragons[i][1]
    else:
        print("NO")
        exit()
print("YES")
