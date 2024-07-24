# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        self._postorderHelper(root, elements)
        return elements

    def _postorderHelper(self, node: Optional[TreeNode], elements: List[int]):
        if node:
            if node.left:
                self._postorderHelper(node.left, elements)
            if node.right:
                self._postorderHelper(node.right, elements)
            elements.append(node.val)