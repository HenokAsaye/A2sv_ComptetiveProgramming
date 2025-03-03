# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summation = ListNode()
        ans =  summation
        current = l1
        l2current = l2
        L1 = []
        L2 = []
        while current:
            L1.append(current.val)
            current =  current.next
        while l2current:
            L2.append(l2current.val)
            l2current =  l2current.next
        print(L1)
        print(L2)
        s = "".join(map(str,L1))
        y = "".join(map(str,L2))
        z = str(int(s) + int(y))
        for i in range(len(z)):
            value = ListNode(int(z[i]))
            ans.next = value
            ans = ans.next
        return summation.next
