class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case: empty arrays
        if not inorder or not postorder:
            return None
            
        N = len(postorder)
        # Create mapping of values to indices for inorder array (not postorder)
        inorder_val_to_idx = {} 
        
        for i, n in enumerate(inorder):
            inorder_val_to_idx[n] = i
            
        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None
                
            # The last element in postorder is the root
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # Find position of root in inorder
            root_idx = inorder_val_to_idx[root_val]
            
            # Calculate size of left subtree
            left_subtree_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            # Left subtree: 
            # - inorder: [in_start, root_idx-1]
            # - postorder: [post_start, post_start+left_subtree_size-1]
            root.left = build(in_start, root_idx-1, post_start, post_start+left_subtree_size-1)
            
            # Right subtree:
            # - inorder: [root_idx+1, in_end]
            # - postorder: [post_start+left_subtree_size, post_end-1]
            root.right = build(root_idx+1, in_end, post_start+left_subtree_size, post_end-1)
            
            return root
            
        return build(0, N-1, 0, N-1)