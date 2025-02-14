# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff=float("inf")
        for k in range(len(nums)-2):
            i,j=k+1,len(nums)-1
            while i<j:
                sum=nums[i] + nums[j] + nums[k]
                if abs(min_diff - target) > abs(sum - target):
                    min_diff=sum
                if(sum > target):
                    j-=1
                elif(sum < target):
                    i+=1
                else:
                    return sum
        return min_diff


            
        