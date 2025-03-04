# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        i=1
        count = 0
        while maxDoubles and target >=2:
            if(target%2 == 0 ):
                count +=1
                maxDoubles -=1
            else:
                count +=2
                maxDoubles -=1
            target = target // 2
        count += (target - i) 
        return count
