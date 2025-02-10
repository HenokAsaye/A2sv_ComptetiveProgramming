# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        n = len(people)
        for i in range(n):
            for j in range(0, n-i-1):
                if people[j][1] < people[j+1][1]:
                    people[j], people[j+1] = people[j+1], people[j]
        sorted_names = [person[0] for person in people]
        return sorted_names
