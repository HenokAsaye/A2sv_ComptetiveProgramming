# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        arr =[int(i) for i in s]
        n=len(arr)
        Lhs = [arr[0]]
        for i in range(1,len(arr)):
            Lhs.append(arr[i]+Lhs[i-1])
        print(Lhs)
        maximum = 0
        zeros = 0
        c_s = 0
        for i in range(len(arr)-1):
            if(arr[i] == 0):
                zeros +=1
            c_s = zeros + (Lhs[(n-1)] - Lhs[(i)])
            maximum = max(c_s,maximum)
        return maximum
