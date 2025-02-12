# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      h=0;
      for i in range(1,len(nums)):
        if (nums[i] !=nums[h]):
            h+=1
            nums[h] = nums[i]
      return h+1 
      return nums[:h] 