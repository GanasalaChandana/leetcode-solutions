# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        self._preorderHelper(root, elements)
        return elements

    def _preorderHelper(self, node: Optional[TreeNode], elements: List[int]):
        if node:
            elements.append(node.val)
            if node.left:
                self._preorderHelper(node.left, elements)
            if node.right:
                self._preorderHelper(node.right, elements)
    