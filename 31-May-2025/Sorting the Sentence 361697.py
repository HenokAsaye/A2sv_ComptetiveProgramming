# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_tuples = [(word[:-1], int(word[-1])) for word in words]
        word_tuples.sort(key=lambda x: x[1])
        return ' '.join(word[0] for word in word_tuples)