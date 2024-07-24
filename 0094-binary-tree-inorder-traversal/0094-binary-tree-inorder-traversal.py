# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        self._inorderHelper(root, elements)
        return elements

    def _inorderHelper(self, node: Optional[TreeNode], elements: List[int]):
        if node:
            if node.left:
                self._inorderHelper(node.left, elements)
            elements.append(node.val)
            if node.right:
                self._inorderHelper(node.right, elements)