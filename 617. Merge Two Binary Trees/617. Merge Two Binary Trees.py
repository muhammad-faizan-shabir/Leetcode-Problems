# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
    
        if(root1 is None and root2 is None):
            current = None
        elif(root2 is None):
            current = TreeNode(root1.val)
            current.left = self.mergeTrees(root1.left,None)
            current.right = self.mergeTrees(root1.right,None)
        elif(root1 is None):
            current = TreeNode(root2.val)
            current.left = self.mergeTrees(root2.left,None)
            current.right = self.mergeTrees(root2.right,None)
        else:
            current = TreeNode(root1.val + root2.val)
            current.left = self.mergeTrees(root1.left,root2.left)
            current.right = self.mergeTrees(root1.right,root2.right)
        
        return current