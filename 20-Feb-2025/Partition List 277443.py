# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater_than = ListNode(None)
        less_than = ListNode(None)
        current = head
        greaterthan_pointer = greater_than
        lessthan_pointer = less_than

        while current:
            value = ListNode(current.val)
            if(current.val < x):
                lessthan_pointer.next = value
                lessthan_pointer = lessthan_pointer.next
            else:
                greaterthan_pointer.next = value
                greaterthan_pointer = greaterthan_pointer.next
            current = current.next
        print(greater_than)
        print(less_than)
        greater_than = greater_than.next
        lessthan_pointer.next = greater_than
        print(greater_than)
        print(less_than)
        return less_than.next
        
        
        
        