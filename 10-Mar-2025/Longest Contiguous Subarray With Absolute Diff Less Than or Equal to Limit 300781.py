# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        m_q = deque()
        min_q = deque()
        left=0
        ans = 0
        for right in range(len(nums)):
            while m_q and m_q[-1] < nums[right]:
                m_q.pop()
            while min_q and min_q[-1] > nums[right]:
                min_q.pop()
            m_q.append(nums[right])
            min_q.append(nums[right])
            while m_q[0] - min_q[0] > limit:
                if nums[left] == m_q[0]:
                    m_q.popleft()
                if nums[left] == min_q[0]:
                    min_q.popleft()
                left+=1
            ans =  max(ans,right-left+1)
        return ans


            




'''
8 2 4 7 





'''