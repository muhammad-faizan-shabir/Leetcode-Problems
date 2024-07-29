# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        head=ListNode(0,None)
        current= head
        while((l1 is not None) and (l2 is not None)):
            sum =carry+ l1.val + l2.val
            carry=sum//10
            sum =sum%10
            
            current.next=ListNode(sum,None)
            current=current.next
            l1=l1.next
            l2=l2.next
        
        
        
        while(l1 is not None):
            sum =carry+l1.val
            carry=sum//10
            sum=sum%10
            current.next=ListNode(sum,None)
            current=current.next
            l1=l1.next

        while(l2 is not None):
            sum =carry+l2.val
            carry=sum//10
            sum=sum%10
            current.next=ListNode(sum,None)
            current=current.next
            l2=l2.next

        if(carry!=0):
            current.next=ListNode(carry)

        head=head.next
        return head




        