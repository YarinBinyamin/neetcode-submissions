# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if ((p == None) and (q== None)):
            return True
        def isSame(p,q):
            if (p == None and q != None) or (p != None and q == None) or p.val != q.val:
                return False
            if (p.left != None and q.left!= None):
                return isSame(p.left, q.left)
            elif((p.left == None and q.left != None) or (p.left != None and q.left == None)):
                return False
            if (p.right != None and q.right!= None):
                return isSame(p.right, q.right)
            elif((p.right == None and q.right != None) or (p.right != None and q.right == None)):
                return False
            return True
        return isSame(p,q)
        