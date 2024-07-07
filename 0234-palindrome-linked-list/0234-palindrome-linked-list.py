class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        fast = head
        slow = head
        
        # Find the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half of the linked list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # Check if the linked list is a palindrome
        left, right = head, prev
        while right:  # Only need to check the right half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
