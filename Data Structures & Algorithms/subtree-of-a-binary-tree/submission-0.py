# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSame(self, r, s):
        if not r and not s:
            return True
        if not r or not s:
            return False
        if r.val == s.val:
            return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or self.isSame(root, subRoot)