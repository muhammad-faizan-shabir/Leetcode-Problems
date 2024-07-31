# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def traverse(root,targetSum,flag):
           if((flag[0]==False) and (root is not None)):
            if((targetSum-root.val)==0 and(root.left==None) and (root.right==None)):
                flag[0]=True
            else:
                traverse(root.left,targetSum-root.val,flag)
                traverse(root.right,targetSum-root.val,flag)


        flag=[False]

        traverse(root,targetSum,flag)

        return flag[0]


        

                
        