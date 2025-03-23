# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={"(":")","{":"}","[":"]"}
        for i in range(len(s)):
            if(s[i] in  mapping):
                stack.append(s[i])
                print(stack)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if s[i] != mapping[a]:
                    return False
        return stack == []   
                


        