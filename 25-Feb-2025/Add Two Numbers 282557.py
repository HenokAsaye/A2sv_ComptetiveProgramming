# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1 = []
        L2 = []
        summation = ListNode()  
        summation_pointer = summation
        current = l1
        l2current = l2
        
        while current:
            L1.append(int(current.val))
            current = current.next
        while l2current:
            L2.append(int(l2current.val))
            l2current = l2current.next
        L1.reverse()
        L2.reverse()
        
        s = "".join(str(digit) for digit in L1)
        y = "".join(str(digit) for digit in L2)
        
        z = str(int(s) + int(y))

        L3 = []
        for k in range(len(z)-1, -1, -1):
            L3.append(z[k])
        for n in range(len(L3)):
            value = ListNode(int(L3[n]))
            summation_pointer.next = value
            summation_pointer = summation_pointer.next
            
        return summation.next

        