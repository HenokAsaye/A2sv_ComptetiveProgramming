# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    key = arr[-1]
    i = n - 2 
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1
        print(*(arr))
    arr[i + 1] = key
    
    print(' '.join(map(str, arr)))

if __name__ == '__main__':  
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
