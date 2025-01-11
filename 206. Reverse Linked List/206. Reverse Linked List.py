# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if(head is not None and head.next is not None):
            current=head
            previous=None
            ahead=None

            while(current is not None):
                ahead=current.next
                current.next=previous
                previous=current
                current=ahead
            
            head=previous
        
        return head



        