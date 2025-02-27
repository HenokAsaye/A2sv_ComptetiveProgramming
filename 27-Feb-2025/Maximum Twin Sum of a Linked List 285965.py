# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        slow =  head
        middle = head
        last = head
        while last and last.next:
            last = last.next.next
            middle = middle.next
        middle_pointer = middle
        prev = None
        while middle_pointer:
            new_value = middle_pointer.next
            middle_pointer.next = prev
            prev = middle_pointer
            middle_pointer = new_value
        prev_pointer = prev
        while prev_pointer:
            summation = prev_pointer.val + slow.val
            max_sum = max(summation,max_sum)
            prev_pointer = prev_pointer.next
            slow = slow.next
        return max_sum


        


        