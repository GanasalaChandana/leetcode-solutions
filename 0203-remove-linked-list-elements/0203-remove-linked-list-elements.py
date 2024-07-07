# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        flag = ListNode(next = head)
        prev, curr = flag, head

        while curr:
            next = curr.next

            if curr.val == val:
                prev.next = next

            else:
                prev = curr
            
            curr = next
        return flag.next #it points to the first element in the list

