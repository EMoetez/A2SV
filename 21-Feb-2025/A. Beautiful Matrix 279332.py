# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix=[]
for row in range(5):
    matrix.append(input().split())
    
for row_idx in range(5):
    for col_idx in range(5):
        if matrix[row_idx][col_idx] == '1':
            print(abs(row_idx-2) + abs(col_idx-2))
            break