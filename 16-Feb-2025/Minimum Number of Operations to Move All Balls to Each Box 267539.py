# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            number_of_moves = 0
            for j in range(len(boxes)):
                if(int(boxes[j]) == 1):
                    number_of_moves += abs(i-j)
            ans.append(number_of_moves)
        return ans


        