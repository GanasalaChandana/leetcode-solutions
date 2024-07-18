# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        result = []
        while len(queue) != 0:
            layer =[]
            for i in range(len(queue)):
                temp = queue.pop(0)
                layer.append(temp.val)
                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)
            result.insert(0,layer) #inserting in a bottom-up level order
        return result
        
        