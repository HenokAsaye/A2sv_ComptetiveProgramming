# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ans = []
        for i in range(len(bills)):
            if(bills[i]==5):
                ans.append(bills[i])
            elif(bills[i] == 10):
                if(ans.count(5)>=1):
                    ans.append(10)
                    ans.remove(5)
                else:
                    return False
            elif(bills[i] == 20):
                if((10 in ans) and ans.count(5)>=1):
                    ans.remove(10)
                    ans.remove(5)
                elif(ans.count(5)>=3):
                    ans.remove(5)
                    ans.remove(5)
                    ans.remove(5)
                else:
                    return False
        return True


   



            
                

            



        



'''
5 5 10 10 20



'''