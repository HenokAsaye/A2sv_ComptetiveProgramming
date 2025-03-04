# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        x = sorted(points, key=lambda n:n[1])
        print(x)
        count = 0
        i=0
        while i<len(x):
            j=i+1
            while  (j<len(x)) and (x[i][1] >= x[j][0]):
                j+=1
            i=j
            count+=1
        return count


                