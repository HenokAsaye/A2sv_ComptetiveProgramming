# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        e_pointer = even
        o_pointer = odd
        current = head
        flag = True
        while current:
            if(flag):
                o_pointer.next = current
                o_pointer = o_pointer.next
                flag = False
            else:
                e_pointer.next = current
                e_pointer = e_pointer.next
                flag= True
            current = current.next
        e_pointer.next = None
        o_pointer.next = even.next
        return odd.next



        
    
