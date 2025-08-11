# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Get sorted list of node values via inorder traversal
        nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Build balanced BST from sorted list
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            new_root = TreeNode(nodes[mid])
            new_root.left = build(left, mid - 1)
            new_root.right = build(mid + 1, right)
            return new_root
        
        return build(0, len(nodes) - 1)