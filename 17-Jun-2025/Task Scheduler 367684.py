# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values()) 
        f_max = max(freq)
        max_count = freq.count(f_max)
        optimized = (f_max - 1) * (n + 1) + max_count
        return max(len(tasks), optimized)