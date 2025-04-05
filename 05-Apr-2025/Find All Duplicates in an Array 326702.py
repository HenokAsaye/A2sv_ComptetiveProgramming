# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        ans = []
        for i in range(len(nums)):
            count[nums[i]] +=1
        for a,b in count.items():
            if b ==2:
                ans.append(a)
        return ans

        