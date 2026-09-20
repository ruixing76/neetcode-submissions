# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(root):
            if not root:
                return 0
            return max(helper(root.left),helper(root.right))+1
        left_height=helper(root.left)
        right_height=helper(root.right)
        d=left_height+right_height
        sub=max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(d,sub)
