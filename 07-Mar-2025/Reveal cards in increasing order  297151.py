# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

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
            


            






'''
17 13 11 2 3 5 7 





2 3 5 7 11 13 17


17 13 11 7 5 3 2 



2 13 3 11 5 17 7



'''