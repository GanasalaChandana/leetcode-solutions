# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root]if root else [])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft() #poping from left , pushing to the right
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = reversed(level) if len(result) % 2 else level # reversing in odd levels only 
            result.append(level)
        return result

        