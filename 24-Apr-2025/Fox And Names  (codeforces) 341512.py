# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

import sys
from collections import defaultdict, deque

def main():
    t = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(t)]

    graph = defaultdict(list)
    in_degree = [0] * 26  

    for i in range(t - 1):
        w1, w2 = words[i], words[i + 1]
        L = min(len(w1), len(w2))
        found = False
        for j in range(L):
            if w1[j] != w2[j]:
                a, b = w1[j], w2[j]
                if b not in graph[a]:
                    graph[a].append(b)
                    in_degree[ord(b) - ord('a')] += 1
                found = True
                break
        if not found and len(w1) > len(w2):
            print("Impossible")
            sys.exit(0)
    q = deque(
        chr(i + ord('a'))
        for i in range(26)
        if in_degree[i] == 0
    )
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            idx = ord(v) - ord('a')
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                q.append(v)
    if len(order) < 26:
        print("Impossible")
    else:
        print(''.join(order))

if __name__ == "__main__":
    main()
