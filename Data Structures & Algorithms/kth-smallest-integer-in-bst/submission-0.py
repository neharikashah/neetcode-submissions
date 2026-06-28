# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, k, res):
        if root:
            
            self.inorder(root.left, k, res)
            res.append(root.val)

            self.inorder(root.right, k, res)



    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root, k , res)
        return res[k-1]