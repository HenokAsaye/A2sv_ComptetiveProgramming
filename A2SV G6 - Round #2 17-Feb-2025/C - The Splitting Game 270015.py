# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
 
    left_counter = Counter()
    right_counter = Counter(s)
    max_distinct = 0
 
    for i in range(1, n):  
        left_counter[s[i - 1]] += 1  
        right_counter[s[i - 1]] -= 1  
 
        if right_counter[s[i - 1]] == 0:
            del right_counter[s[i - 1]]  
 
        max_distinct = max(max_distinct, len(left_counter) + len(right_counter))  
 
    print(max_distinct)