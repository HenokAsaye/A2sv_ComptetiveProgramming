# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backTrack(s, target, index):
            if index == len(s):
                return target == 0  
            
            num = 0
            for j in range(index, len(s)):
                num = num * 10 + int(s[j])  
                if num > target:  
                    break
                if backTrack(s, target - num, j + 1):
                    return True
            return False  
        
        total_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if backTrack(square_str, i, 0):  
                total_sum += i * i  
        
        return total_sum
