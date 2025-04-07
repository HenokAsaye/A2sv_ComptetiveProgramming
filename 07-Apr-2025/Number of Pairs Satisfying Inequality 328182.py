# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        a = [x - y for x, y in zip(nums1, nums2)]
        
        def mrg(s, e):
            if s >= e: return 0
            m = (s + e) // 2
            cnt = mrg(s, m) + mrg(m + 1, e)
            j = m + 1
            for i in range(s, m + 1):
                while j <= e and a[i] > a[j] + diff:
                    j += 1
                cnt += e - j + 1
            a[s:e + 1] = sorted(a[s:e + 1])
            return cnt
        
        return mrg(0, len(a) - 1)
