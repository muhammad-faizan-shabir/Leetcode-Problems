# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def getMaxDepth(root):
            if(root is not None):
                return 1 +  max(getMaxDepth(root.left),getMaxDepth(root.right))
            else:
                return 0
            
        return getMaxDepth(root)
        