# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    swap = 0
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:  
                swap += 1  
                a[j], a[j + 1] = a[j + 1], a[j]  
    
    
    b = f"Array is sorted in {swap} swaps."
    c = f"First Element: {a[0]}"
    d = f"Last Element: {a[-1]}"
    
    return b, c, d

if __name__ == '__main__':  
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = countSwaps(a)
    for res in result:
        print(res)