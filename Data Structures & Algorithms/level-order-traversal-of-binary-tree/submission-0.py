# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            q_len=len(q)
            cur_level=[]
            for i in range(q_len):
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    cur_level.append(node.val)
            if cur_level:
                res.append(cur_level)
        return res