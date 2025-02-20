# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

import sys
from collections import defaultdict

n = int(input()) 

for _ in range(n):
    tests_num = int(input())  
    a = list(map(int, input().split()))  
    freq = defaultdict(int)  
    summ = 0
    for i in range(tests_num):
        diff = a[i] - i  
        summ += freq[diff]  
        freq[diff] += 1 
    print(summ)
