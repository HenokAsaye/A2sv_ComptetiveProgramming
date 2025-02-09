# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count =  Counter(answers)
        print(count)
        summation = 0
        for i,j in count.items():
            z = math.ceil((j) / (int(i)+1))
            summation += (z * (int(i)+1))
        return summation



