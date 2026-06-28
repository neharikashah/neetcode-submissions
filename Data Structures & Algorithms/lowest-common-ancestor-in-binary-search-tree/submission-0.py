class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or root.val == p.val or root.val == q.val:
            return root


        l = self.lowestCommonAncestor(root.left, p ,q)
        r = self.lowestCommonAncestor(root.right, p ,q)

        if l and r:
            return root

        if l == None and r == None:
            return None
        
        if l :
            return l
        else:
            return r