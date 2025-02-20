# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second =  head
        while first and first.next:
            first = first.next.next
            second = second.next
            if first == second:
                break
        else:
            return None
        second = head
        while second != first:
            first = first.next
            second = second.next
        return second
        