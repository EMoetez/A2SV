# Problem: Books - https://codeforces.com/contest/279/problem/B

n, m = map(int, input().split())  
a = list(map(int, input().split()))  
i,j = 0,0 
current_sum = 0  
max_books = 0  

while j < n:  
    current_sum += a[j] 

    while current_sum > m:  
        current_sum -= a[i]  
        i += 1  

    max_books = max(max_books, j - i + 1) 
    j += 1
print(max_books)
