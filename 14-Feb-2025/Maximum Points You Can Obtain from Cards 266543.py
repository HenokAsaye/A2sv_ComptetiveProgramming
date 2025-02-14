# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = sum(cardPoints)
        window = 0
        if k == len(cardPoints):
            return total_sum
        for i in range(len(cardPoints)-k):
            window+=cardPoints[i]
        min_sum = window
        left = 0
        print(window)
        for right in range(len(cardPoints)-k,len(cardPoints)):
            window +=cardPoints[right]
            window -=cardPoints[left]
            left+=1
            min_sum = min(window,min_sum)
        return total_sum - min_sum

