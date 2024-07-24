# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True  #if both are empty
        if not p or not q or p.val != q.val:
            return False  #if either one of the node is empty and other one is having some value
        return (self.isSameTree(p.left,q.left) and
        self.isSameTree(p.right,q.right))  # if both the values are same

       
