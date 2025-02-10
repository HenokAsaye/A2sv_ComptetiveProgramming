# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, images: List[List[int]]) -> List[List[int]]:
        x = [list(reversed([images[i][j] for j in range(len(images[0]))])) for i in range(len(images))]
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j] == 0:
                    x[i][j] =1
                else:
                    x[i][j] =0
        
        return x