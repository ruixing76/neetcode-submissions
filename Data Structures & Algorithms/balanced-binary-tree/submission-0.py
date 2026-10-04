# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balance=True
        def getHeight(node):
            nonlocal is_balance
            if not node:
                return 0
            left_height=getHeight(node.left)
            right_height=getHeight(node.right)
            if abs(left_height-right_height)>1:
                is_balance=False
            return max(left_height,right_height)+1
        getHeight(root)
        return is_balance