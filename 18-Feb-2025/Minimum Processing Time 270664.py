# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        maximum = 0
        j=0
        for i in range(3,len(tasks),4):
            maximum = max(maximum,tasks[i]+processorTime[j])
            j+=1
        return maximum





