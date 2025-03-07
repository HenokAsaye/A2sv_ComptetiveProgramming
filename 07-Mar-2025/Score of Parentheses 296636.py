# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0  
        depth = 0  

        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                depth += 1  
            else:  
                stack.pop()
                depth -= 1  
                if s[i - 1] == '(':
                    score += 2 ** depth  

        return score
