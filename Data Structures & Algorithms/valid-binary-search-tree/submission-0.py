# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True
        def rec(node, min_val, max_val):
            if node is None :
                return True
            if not (min_val < node.val < max_val):
                return False

            left_ok = rec(node.left, min_val, node.val)
            right_ok = rec(node.right, node.val, max_val)

            return left_ok and right_ok
        return rec(root, float("-inf"),float("inf")) 