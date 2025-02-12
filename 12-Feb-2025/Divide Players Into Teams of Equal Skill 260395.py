# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        sum=skill[i] + skill[j]
        product=0
        while i < j:
            if(skill[i] + skill[j] == sum):
                product+=(skill[i]*skill[j])
                i+=1
                j-=1
            else:
                return -1
        return product
        