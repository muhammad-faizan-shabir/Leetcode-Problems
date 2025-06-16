"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if(root is not None):
            lst = [root.val]
            
            if(root.children is not None):
                for child in root.children:
                    lst = lst + self.preorder(child)
            
            return lst
        
        return []