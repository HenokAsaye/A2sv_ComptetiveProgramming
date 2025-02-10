# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=sorted(nums)
        for i in range(len(n)):
            count=0
            for j in (n):
                if(nums[i]>j):
                    count+=1
            nums[i]=count
        return nums