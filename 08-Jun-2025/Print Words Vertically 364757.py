# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_word_length = max(map(len, words))
        
        return [
            ''.join(word[i] if i < len(word) else ' ' for word in words).rstrip()
            for i in range(max_word_length)
        ]


        

