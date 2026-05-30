# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if  not root:
            return []
        ans = []
        def rec(depth , node):
            if len(ans) == depth:
                ans.append([])
            ans[depth].append(node.val)
            if node.left :
                rec(depth +1 , node.left)
            if node.right :
                rec(depth +1 , node.right)
        
        rec(0,node=root)
        return ans