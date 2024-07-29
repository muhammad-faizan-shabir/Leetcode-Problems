# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(list1 is None and list2 is None):
            return None
        elif(list1 is None):
            return list2
        elif(list2 is None):
            return list1

        head=None

        if(list1.val<=list2.val):
            head = list1
            list1=list1.next
        else:
            head = list2
            list2=list2.next
        
        current=head
        
        while((list1 is not None) and(list2 is not None)):
            if(list1.val<=list2.val):
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        
        while(list1 is not None):
            current.next =list1
            list1=list1.next
            current=current.next
        
        while(list2 is not None):
            current.next=list2
            list2=list2.next
            current = current.next
        
        return head



        
        