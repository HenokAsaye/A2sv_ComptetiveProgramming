# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1


class Solution: 
    def selectionSort(self, nums):
        #code here
        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1,len(nums)):
                if(nums[min_index] > nums[j]):
                    nums[min_index],nums[j] = nums[j] , nums[min_index]
        return nums
