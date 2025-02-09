# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        b = [set() for _ in range(9)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                x = nums[i][j]
                if(x == "."):
                    continue
                if(x in r[i]):
                    return False
                r[i].add(x)
                if (x in c[j]):
                    return False
                c[j].add(x)
                bi = (i//3)*3 + (j//3)
                if(x in b[bi]):
                    return False
                b[bi].add(x)
        return True