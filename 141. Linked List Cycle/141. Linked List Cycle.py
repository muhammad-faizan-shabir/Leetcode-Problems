# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        dictionary={}
        cycleExists=False

        while((cycleExists==False) and (head is not None)):
            dictionary[id(head)]= dictionary.get(id(head),0) +1
            if(dictionary[id(head)]>1):
                cycleExists=True
            head=head.next

        return cycleExists

        
        