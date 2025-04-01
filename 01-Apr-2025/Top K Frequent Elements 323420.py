# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        array = [[] * k for k in range(max(dic.values())+1)]
        print(array)
        print(dic)
        for i in dic:
            array[dic[i]].append(i)
        ans = []
        j=len(array)-1
        print(array)
        while k>0:
            ans.extend(array[j])
            k-=len(array[j])
            j-=1
        return ans