# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head 
        cur = head
        prev, last = None, None  
        p_pointer = prev
        last_pointer = last
        length = 0
        counter = head
        while counter:
            length += 1
            counter = counter.next
        rem = length % k
        stop = length - rem  
        temp_head = head
        for _ in range(k):
            if not cur:
                return head  
            new_value = cur.next
            cur.next = p_pointer
            p_pointer = cur
            cur = new_value
        cnt = k
        head_2 = p_pointer  
        temp = head_2
        for _ in range(k - 1):
            temp = temp.next
        if cnt == stop:
            temp.next = cur  
            return head_2 
        
        last_pointer = None 
        while cur:
            if cnt + k > length:  
                temp.next = cur
                return head_2
            for _ in range(k):
                new_value = cur.next
                cur.next = last_pointer
                last_pointer = cur
                cur = new_value
            
            temp.next = last_pointer  
            cnt += k
            for _ in range(k):
                temp = temp.next

            if cnt == stop:
                temp.next = cur
                return head_2
            
        return head_2  
