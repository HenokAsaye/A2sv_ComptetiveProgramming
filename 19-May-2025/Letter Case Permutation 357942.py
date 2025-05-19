# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = []
        for i, ch in enumerate(s):
            if ch.isalpha():
                letters.append(i)  # store indices of letters
        
        n = len(letters)
        result = []
        total = 1 << n  # 2^n combinations

        for bits in range(total):
            chars = list(s)
            for j in range(n):
                index = letters[j]
                if bits & (1 << j):
                    chars[index] = chars[index].upper()
                else:
                    chars[index] = chars[index].lower()
            result.append("".join(chars))
        
        return result
