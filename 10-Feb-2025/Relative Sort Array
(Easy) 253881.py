# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = defaultdict(int)
        for i in range(len(arr2)):
            count[arr2[i]] = arr1.count(arr2[i])
        print(count)
        ans = []
        for j,k in count.items():
            while k>0:
                ans.append(j)
                k-=1
        print(ans)  
        arr1.sort()
        for l in arr1:
            if l not in arr2:
                ans.append(l)
        return ans


        