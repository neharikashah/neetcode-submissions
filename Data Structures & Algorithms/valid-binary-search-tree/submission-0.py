# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, pre):
        if not root :
            return True
        if not self.inorder(root.left, pre):
            return False
        if pre[0] >= root.val:
            return False
        pre[0] = root.val
        return self.inorder(root.right, pre)

        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = [-(2**63)]

        return self.inorder(root, pre)