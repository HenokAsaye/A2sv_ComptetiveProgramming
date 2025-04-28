# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(nums,n,i):
            largest = i
            left_child = 2*i +1
            right_child = 2*i +2
            if(left_child < n) and (nums[largest] < nums[left_child]):
                largest = left_child
            if(right_child < n) and (nums[largest] < nums[right_child]):
                largest = right_child
            if(largest != i):
                nums[largest],nums[i] = nums[i], nums[largest]
                heapify(nums,n,largest)
        n = len(nums)
        for i in range((n-1)//2,-1,-1):
            heapify(nums,n,i)
        for i in range(n-1,0,-1):
            nums[0],nums[i] = nums[i],nums[0]
            heapify(nums,i,0)
        return nums[-k]

