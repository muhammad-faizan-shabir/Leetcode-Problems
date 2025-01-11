# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check(left,right,flag):
            if(flag[0]==True):
                if((left is not None) and(right is not None)):
                    if(left.val!=right.val):
                        flag[0]=False
                    
                    check(left.left,right.right,flag)
                    check(right.left,left.right,flag)
                else:
                    if((left is None) and(right is not None)):
                        flag[0]=False
                    if((left is not None)and(right is None)):
                        flag[0]=False
        
        flag=[True]

        check(root.left,root.right,flag)

        return flag[0]




        