# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
 
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
 
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
 
    total_sum = prefix_sum[n]
    results = []
 
    for _ in range(q):
        l, r, k = map(int, input().split())
        subarray_sum = prefix_sum[r] - prefix_sum[l - 1]
        new_sum = total_sum - subarray_sum + (r - l + 1) * k
        results.append("YES" if new_sum % 2 else "NO")
 
    print("\n".join(results))