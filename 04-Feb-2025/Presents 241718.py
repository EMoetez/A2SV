# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n=int(input())
pres=input().split()
 
res=[0]*n
for i in range(len(pres)):
    res[int(pres[i])-1]=str(int(i)+1)
 
print(' '.join(res))