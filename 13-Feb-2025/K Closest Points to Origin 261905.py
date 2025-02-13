# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        c = []
        x,y = 0,0
        for i in range(len(points)):
            a = abs(points[i][0] -x)
            b = abs (points[i][1] -y)
            z = (a**2 + b**2)
            c.append([z,points[i]])
        c.sort()
        ans = []
        i=0
        while k>0:
            ans.append(c[i][1])
            i+=1
            k-=1
        return ans



        



        