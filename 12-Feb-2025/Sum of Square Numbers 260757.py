# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = int(c**0.5)
        i=0
        while i <=j:
            if(i**2 + j**2 ==c):
                return True
            elif(i**2 + j**2 <c):
                i+=1
            elif(i**2 + j**2 >c):
                j-=1
        return False

            
                    



            
        