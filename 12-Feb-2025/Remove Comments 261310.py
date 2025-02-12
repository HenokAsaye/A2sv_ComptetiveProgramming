# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source):
        result = []
        in_block = False
        newline = ""
        for line in source:
            i = 0
            if not in_block:
                newline = ""
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 2  
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 2  
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break  
                elif not in_block:
                    newline += line[i]
                    i += 1
                else:
                    i += 1  
            if not in_block and newline:
                result.append(newline)
        
        return result
