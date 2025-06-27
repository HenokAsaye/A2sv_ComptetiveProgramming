# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        if len(nums2) % 2 == 1:
            xor1 = reduce(operator.xor, nums1, 0)
        xor2 = 0
        if len(nums1) % 2 == 1:
            xor2 = reduce(operator.xor, nums2, 0)
        return xor1 ^ xor2
