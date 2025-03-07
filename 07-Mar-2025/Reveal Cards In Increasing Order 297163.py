# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort() 
        q = deque()
        for i in range(len(deck)):
            q.append(i)
        ans = [0] * len(deck)
        for  num in  deck:
            ans[q.popleft()] = num
            if q:
                x = q.popleft()
                q.append(x)
        return ans