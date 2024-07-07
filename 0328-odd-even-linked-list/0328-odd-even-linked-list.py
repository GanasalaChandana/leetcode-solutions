# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd = head
        even = odd.next
        even_head = even
        while even != None and even.next != None:
            odd.next = even.next #1->3
            odd = odd.next  #odd = 3
            even.next = odd.next #2->4
            even = even.next # even = 4
        odd.next = even_head #5->2
        return head




           