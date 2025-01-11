# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def inOrderTraversal(p,q,flag):
            if(flag[0]==True):
                if((p is not None) and(q is not None)):
                    inOrderTraversal(p.left,q.left,flag)
                    if(p.val!=q.val):
                        flag[0]=False
                    inOrderTraversal(p.right,q.right,flag)
                else:
                    if((p is None) and (q is not None)):
                        flag[0]= False
                    if((q is None) and (p is not None)):
                        flag[0]= False
        
        flag=[True]
        inOrderTraversal(p,q,flag)

        return flag[0]
        