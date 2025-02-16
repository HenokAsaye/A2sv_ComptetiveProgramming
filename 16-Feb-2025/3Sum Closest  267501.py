# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_difference = float("inf")
        for j in range(len(nums)-2):
            i,k = j+1,len(nums)-1
            while i<k:
                summation = nums[i] + nums[k] +nums[j]
                if(abs(summation-target)  < abs(min_difference - target)):
                    min_difference = summation
                if(summation > target):
                    k-=1
                elif(summation < target):
                    i+=1
                else:
                    return summation
        return min_difference



            
        
        
                
            


            
        