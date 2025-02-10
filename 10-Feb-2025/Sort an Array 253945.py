# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            left_arr = nums[:len(nums)//2]
            right_arr = nums[len(nums)//2:len(nums)]

            self.sortArray(left_arr)
            self.sortArray(right_arr)
            nums.clear();
            
            i = 0
            j = 0
            
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    nums.append(left_arr[i])
                    i += 1
                else:
                    nums.append(right_arr[j])
                    j += 1

            while i < len(left_arr):
                nums.append(left_arr[i])
                i += 1

            while j < len(right_arr):
                nums.append(right_arr[j])
                j += 1

        return nums