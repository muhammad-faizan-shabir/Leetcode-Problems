class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        aLength= len(a)
        bLength=len(b)
        carry=0
        aIterator=aLength-1
        bIterator=bLength-1
        result=""

        while(aIterator>=0 and bIterator>=0):
            sum = int(a[aIterator]) + int(b[bIterator]) +carry
            result= str(sum%2) +result
            carry = sum//2
            aIterator=aIterator-1
            bIterator=bIterator-1
        
        while(aIterator>=0):
            sum= int(a[aIterator])+carry
            result= str(sum%2) + result
            carry = sum//2
            aIterator=aIterator-1
        
        while(bIterator>=0):
            sum = int(b[bIterator]) +carry
            result= str(sum%2) + result
            carry = sum//2
            bIterator=bIterator-1
        
        if(carry!=0):
            result = str(carry) + result

        return result
        