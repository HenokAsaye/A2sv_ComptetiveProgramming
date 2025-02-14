# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        new =list(s)
        count_zero = 0
        ans = 0
        for j in range(len(new)-1,-1,-1):
            if(int(new[j]) ==0):
                count_zero +=1
            elif(int(new[j])==1):
                ans +=count_zero
        return ans




        


        