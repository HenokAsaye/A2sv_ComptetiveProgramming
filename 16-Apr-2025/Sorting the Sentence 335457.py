# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        count = defaultdict(str)
        arr = s.split()
        for word in arr:
            index = int(word[-1])
            count[index] = word[:-1]
        result = [count[i] for i in range(1, len(arr)+1)]
        return ' '.join(result)


