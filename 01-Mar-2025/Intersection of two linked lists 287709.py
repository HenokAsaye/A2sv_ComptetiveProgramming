# Problem: Intersection of two linked lists - https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first= headA
        second=headB
        v=set()
        while first:
            v.add(first)
            first=first.next
        while second:
            if second in v:
                return second
            else:
                second=second.next
        return None
  