# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        min_height = min(heights)
        max_height = max(heights)
        _range = max_height - min_height +1
        people =[[] for i in range(_range)]
        for name,height in zip(names,heights):
            people[height - min_height].append(name)
        sorted_names=[]
        for i in range(_range-1,-1,-1):
            sorted_names.extend(people[i])
        return sorted_names

        

