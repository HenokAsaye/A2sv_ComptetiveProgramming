# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i,a in  enumerate(nums):
            if i> 0  and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum = a + nums[l] + nums[r]
                if sum>0:
                    r-=1
                elif sum <0:
                    l+=1
                else:
                    answer.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
        return answer


