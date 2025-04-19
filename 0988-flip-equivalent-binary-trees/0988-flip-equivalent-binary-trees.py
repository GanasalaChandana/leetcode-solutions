# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
    # If both are None, they are equivalent
        if not r1 and not r2:
         return True
    
    # If only one is None or values don't match, they are not equivalent
        if not r1 or not r2 or r1.val != r2.val:
         return False
        
    # Try both arrangements - original and flipped
        a = self.flipEquiv(r1.left, r2.left) and self.flipEquiv(r1.right, r2.right)
        b = self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)
    
        return a or b

        