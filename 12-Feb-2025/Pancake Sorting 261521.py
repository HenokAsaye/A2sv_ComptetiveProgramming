# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for target in range(n, 0, -1):  
            max_idx = arr.index(target)  
            
            if max_idx == target - 1:
                continue  
            if max_idx != 0:
                res.append(max_idx + 1)  
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
            res.append(target)  
            arr[:target] = reversed(arr[:target])
        return res

        