# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        prev=None
        current=head

        while(current is not None):
            if(current.val==val):
                if(prev is None):
                    head=current.next
                    current=head
                else:
                    current=current.next
                    prev.next=current
            else:
                prev=current
                current=current.next
        
        return head