# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        previous = None
        current = head
        while current:
            current_value = current.val
            temporary = ListNode(current_value)
            temporary.next = previous
            previous = temporary
            current = current.next
        while temporary and head:
            if temporary.val != head.val:
                return False
            temporary = temporary.next
            head = head.next
        return True





        