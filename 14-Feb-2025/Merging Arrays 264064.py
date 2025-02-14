# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
 
def mergeSortedArray(first, second):
    i = 0
    j = 0
    ans = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            ans.append(first[i])
            i += 1
        else:
            ans.append(second[j])
            j += 1
    while i < len(first):
        ans.append(first[i])
        i += 1
    while j < len(second):
        ans.append(second[j])
        j += 1
    return ans
merged_array = mergeSortedArray(first, second)
print(" ".join(map(str, merged_array)))