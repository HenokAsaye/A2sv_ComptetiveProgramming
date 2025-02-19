# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
        third = ListNode(-1,None)
        current = third
        print(third)
        while first and second:
            if(first.val < second.val):
                value = ListNode(first.val)
                current.next = value
                first =  first.next
            else:
                value = ListNode(second.val)
                current.next =value
                second = second.next
            current = current.next
        if(first):
            current.next = first
        if(second):
            current.next = second
        return third.next

            

        