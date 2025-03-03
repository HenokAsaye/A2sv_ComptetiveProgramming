# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

import sys
def solve():
    t = int(sys.stdin.readline().strip())  
    results = []
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        indexed_a = sorted(enumerate(a), key=lambda x: x[1])  
        sorted_b = sorted(b)  
        result = [0] * n  
        for (original_index, _), b_value in zip(indexed_a, sorted_b):
            result[original_index] = b_value  
        results.append(" ".join(map(str, result)))
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    solve()