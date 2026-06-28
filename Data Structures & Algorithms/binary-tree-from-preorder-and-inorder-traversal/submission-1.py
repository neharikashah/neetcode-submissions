# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createTree(self, preorder, prs, pre, inorder, ins, ine):
        if ins> ine: 
            return None

        node = TreeNode(preorder[prs])
        position = -1
        for i in range(ins, ine + 1):
            if inorder[i] == preorder[prs]:
                position = i
                break

        lins = ins
        line = position -1
        lpres = prs + 1
        #nding index = start + size - 1
        lpree = lpres + (line - lins + 1) -1
         

        rpres = lpree + 1
        rpree = pre
        rins = position + 1
        rine = ine

        node.left = self.createTree(preorder, lpres, lpree, inorder, lins, line)
        node.right = self.createTree(preorder, rpres, rpree, inorder, rins, rine)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)

        return self.createTree(preorder, 0, n-1, inorder, 0, n-1)
