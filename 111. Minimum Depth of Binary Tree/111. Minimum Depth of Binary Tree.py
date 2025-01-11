# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def getMinDepth(root):
            if(root is not None):
                if((root.left is None) and (root.right is None)):
                    return 1
                elif((root.left is None)and(root.right is not None)):
                    return 1 + getMinDepth(root.right)
                elif((root.left is not None)and(root.right is None)):
                    return 1 + getMinDepth(root.left)
                else:
                    return 1 + min(getMinDepth(root.left),getMinDepth(root.right))
            else:
                return 0
                
        
        return getMinDepth(root)
        
        