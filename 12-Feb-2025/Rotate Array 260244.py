# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %=n
        i,j = 0,n-1
        while i <j:
            nums[i],nums[j] = nums[j] , nums[i]
            i+=1
            j-=1
        print(nums)
        start,end =0,k-1
        while start < end:
            nums[start] , nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        a=k
        b=n-1
        print(nums)
        while a < b:
            nums[a],nums[b] = nums[b] , nums[a]
            a+=1
            b-=1
        

        