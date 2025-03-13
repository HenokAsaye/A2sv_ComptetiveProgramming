# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0
        i=0
        while i<len(s):
            if s[i].isdigit():
                temp = ""
                while s[i].isdigit():
                    temp +=s[i]
                    i+=1
                num = int(temp)
                i-=1
            elif(s[i] == "["):
                stack.append(curr)
                stack.append(num)
                print(stack)
                curr = ""
                num = 0
            elif(s[i] == "]"):
                num = stack.pop()
                prev = stack.pop()
                curr = prev + curr * num
            else:
                curr += s[i]
            i+=1
        return curr





