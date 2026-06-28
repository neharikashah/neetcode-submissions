# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxpath(self, root, max_val):
        if root == None:
            return 0

        l = self.maxpath(root.left, max_val)
        r = self.maxpath(root.right, max_val)

        if l<0:
            l = 0 
        if r<0:
            r = 0

        self.max_val = max(self.max_val, l+r+root.val)
        return max(l, r) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = -100000

        
        
        s = self.maxpath(root, self.max_val)
        return int(self.max_val)