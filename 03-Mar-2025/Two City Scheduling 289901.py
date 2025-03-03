# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        x = sorted(costs, key=lambda item:abs(item[1]-item[0]),reverse = True )
        print(x)
        A = 0
        sum = 0
        b = 0
        i=0
        while i < len(x):
            z = min(x[i][0], x[i][1])
            print(z)
            if(z == x[i][0]):
                A += 1
                sum += z
            else:
                sum += z
                b += 1
            i+=1
            if A == len(x) // 2:
                while i < len(x):
                    sum += x[i][1]
                    i+=1
                break
            if b == len(x) // 2:
                while i < len(x):
                    sum += x[i][0]
                    i+=1
                break
            
        return sum
            



        