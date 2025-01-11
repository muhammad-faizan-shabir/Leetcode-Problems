# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def postorderTraversal(root,output):
            if(root is not None):
                postorderTraversal(root.left,output)
                postorderTraversal(root.right,output)
                output.append(root.val)
                
        output=[]
        postorderTraversal(root,output)

        return output