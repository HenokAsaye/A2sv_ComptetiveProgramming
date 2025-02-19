# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(next=head)
        first = second = dummyNode
        for _ in range(n):
            first =first.next
        while first.next:
            second, first = second.next, first.next
        second.next = second.next.next
        return dummyNode.next


