# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]  
        ans = []

        while left <= right:
            mid = (left + right) // 2
            count, last_position = 1, position[0]  
            
            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        break  

            if count >= m:  
                ans.append(mid)  
                left = mid + 1  
            else:
                right = mid - 1  
        
        print(ans)  
        return right  


