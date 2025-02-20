# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans =[0]*(1001)
        for i,j,k in trips:
            ans[j]+=i
            ans[k] -=i
        for i in range(len(ans)):
            ans[i] += ans[i-1]
        print(ans)
        if(max(ans) > capacity):
            return False
        else:
            return True

        
            