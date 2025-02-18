# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        prefix_sum=[beans[0]]
        for i in range(1, len(beans)):
            prefix_sum.append(beans[i] + prefix_sum[i-1])
        prefix_sum = [0] + prefix_sum + [0]
        print(prefix_sum)
        minimum = float("inf")
        for i in range(len(beans)):
            c_d = prefix_sum[i] 
            x = prefix_sum[-2] - prefix_sum[i + 1] - beans[i] * (n - i - 1)
            minimum = min(minimum,c_d + x)
        return minimum

                                                                  
