# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if root is None:
            return []
        
        paths = []
        s = []
        s.append((root, [str(root.val)]))
        
        while(len(s)!=0):
            current = s.pop(0)
            
            if(current[0].left is not None):
                s.append((current[0].left ,current[1] + [str(current[0].left.val)]))
            if(current[0].right is not None):
                s.append((current[0].right ,current[1] + [str(current[0].right.val)]))
            if(current[0].left is None and current[0].right is None):
                paths.append("->".join(current[1]))
        
        return paths