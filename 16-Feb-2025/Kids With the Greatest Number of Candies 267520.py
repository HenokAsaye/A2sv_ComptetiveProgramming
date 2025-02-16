# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, nums: List[int], extra: int) -> List[bool]:
        x = max(nums)
        for i in range(len(nums)):
            if(nums[i]+extra >= x):
                nums[i] = True
            else:
                nums[i] = False
        return nums


        