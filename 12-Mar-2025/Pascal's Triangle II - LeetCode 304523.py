# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def summation(arr):
            ans = []
            for i in range(len(arr)-1):
                ans.append(arr[i]+arr[i+1])
            return [1] + ans +[1]
        def pascal(rowIndex):
            if(rowIndex==0):
                return [1]
            previous = pascal(rowIndex-1)
            return summation(previous)
        return pascal(rowIndex)
            
        