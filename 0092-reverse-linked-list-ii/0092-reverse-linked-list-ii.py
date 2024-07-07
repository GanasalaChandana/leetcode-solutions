# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        flag = ListNode(0, head)
        
     # reach node at position "left"
        leftprev, cur = flag, head
        for i in range (left-1):
            leftprev , cur = cur, cur.next
    # reverse from left to right where cur = "left" and leftprev = "right before left"
        prev = None
        for i in range(right-left+1):
            tmpnext = cur.next
            cur.next = prev
            prev , cur = cur, tmpnext

        leftprev.next.next = cur
        leftprev.next = prev
        return flag.next