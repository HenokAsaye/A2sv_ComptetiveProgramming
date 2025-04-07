# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

import sys
import bisect

input_data = sys.stdin.read().strip().split()
it = iter(input_data)
t = int(next(it))
out_lines = []
for _ in range(t):
    n = int(next(it))
    m = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    b = [int(next(it)) for _ in range(m)]
    b.sort()  
    possible = True
    L = -10**18 
    for ai in a:
        cand1 = ai if ai >= L else 10**18 
        idx = bisect.bisect_left(b, L + ai)
        if idx < len(b):
            cand2 = b[idx] - ai
        else:
            cand2 = 10**18  
        best = min(cand1, cand2)
        if best == 10**18:
            possible = False
            break
        L = best  
    out_lines.append("YES" if possible else "NO")
sys.stdout.write("\n".join(out_lines))
