# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        path = []
        def backTrack(path):
            if len(path) == n:
                flag = True
                for i in range(1,len(path)):
                    if(path[i]== path[i-1]=="0"):
                        flag = False
                        break
                if(flag):
                    ans.append("".join(path))
                else:
                    pass
                return
            path.append("0")
            backTrack(path)
            path.pop()

            path.append("1")
            backTrack(path)
            path.pop()
        backTrack([])
        return ans
      
            
