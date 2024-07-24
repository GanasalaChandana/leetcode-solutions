# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root:
            s = str(root.val)
            m = root
            a = []
            self.helper(root, s, a, m)
            return a

    def helper(self, root, s, a, m):
        flag = 1
        if root.left:
            self.helper(root.left, s+ '->' + str(root.left.val), a, m)
        if root.right:
            self.helper(root.right, s+ '->' + str(root.right.val), a, m)
        else:
            if a:
                for i in a:
                    if s in i:
                        flag = 0
            if flag: a.append(s)
            s = str(m.val)
            flag = 1