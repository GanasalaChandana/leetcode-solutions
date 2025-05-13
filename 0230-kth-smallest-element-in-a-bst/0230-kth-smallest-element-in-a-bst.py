class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        # The condition should be "cur or stack", not "cur and stack"
        while cur or stack:
            # Travel to the leftmost node
            while cur:
                stack.append(cur)
                cur = cur.left
                
            # Process current node
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            # Move to right subtree
            cur = cur.right
        
        # If k is greater than the number of nodes
        return -1  # Or appropriate error handling