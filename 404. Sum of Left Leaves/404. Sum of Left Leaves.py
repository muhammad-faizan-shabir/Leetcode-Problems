# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def sumOfLeftLeaves(root,isLeft):
            if(root is not None):
                if(isLeft and (root.left is None) and (root.right is None)):
                    return root.val
                else:
                    return sumOfLeftLeaves(root.left,True) + sumOfLeftLeaves(root.right,False)
            else:
                return 0

        return sumOfLeftLeaves(root,False)        