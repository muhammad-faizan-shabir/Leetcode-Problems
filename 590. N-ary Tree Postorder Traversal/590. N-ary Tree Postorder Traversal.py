"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if(root is not None):
            lst = []
            
            if(root.children is not None):
                for child in root.children:
                    lst = lst + self.postorder(child)
            
            return lst + [root.val]
        
        return []