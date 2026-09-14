# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def myBuild(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left>preorder_right:
                return None
            preorder_root=preorder_left
            inorder_root=inorder_index[preorder[preorder_root]]

            root=TreeNode(preorder[preorder_root])
            size_left_subtree=inorder_root-inorder_left

            # when we generate next sub array of preorder and inorder
            # left subtree boundary: for preorder, is preorder_left+1:preorder_left+tree_size; for inorder is inorder_left:inorder_root
            # right subtree: for preorder is preorder_left+tree_size+1:right; for inorder is 
            root.left=myBuild(preorder_left+1,preorder_left+size_left_subtree,inorder_left,inorder_root-1)
            root.right=myBuild(preorder_left+size_left_subtree+1,preorder_right,inorder_root+1,inorder_right)
            return root
        n = len(preorder)
        inorder_index={element:i for i,element in enumerate(inorder)}
        return myBuild(0,n-1,0,n-1)