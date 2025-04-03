# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        for i in range(1,len(nums)+1):
            if i in dic:
                dic[i] = 0
            if i not in dic:
                dic[i] = 1
        ans = []
        for i,j in dic.items():
            if j!=0:
                ans.append(i)
        return ans
        

        