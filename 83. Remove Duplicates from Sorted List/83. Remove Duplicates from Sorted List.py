# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if(head is None):
            return head
        
        ptr1= head
        ptr2=head.next

        while(ptr2 is not None):
            if(ptr1.val==ptr2.val):
                ptr2=ptr2.next
            else:
                ptr1.next=ptr2
                ptr1=ptr2
                ptr2=ptr2.next
        
        ptr1.next=None

        return head