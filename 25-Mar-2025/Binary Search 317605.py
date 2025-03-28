# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while right >= left:
            mid =(right  + left) //2
            if(target > nums[mid]):
                left = mid +1
            elif (target < nums[mid]):
                right = mid - 1
            else:
                return mid
        return -1
        
                
        