# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        dictionary={}

        while(headA is not None):
            dictionary[id(headA)]= dictionary.get(id(headA),0) + 1
            headA=headA.next
        
        intersection=None

        while((intersection is None) and (headB is not None)):
            dictionary[id(headB)]=  dictionary.get(id(headB),0) +1
            if(dictionary[id(headB)]>1):
                intersection=headB
            headB=headB.next
        
        return intersection