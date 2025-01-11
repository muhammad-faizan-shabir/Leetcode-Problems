class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digitsLength=len(digits)
        carry=1
        i=digitsLength-1
        
        while(i>=0 and carry!=0):
            num=digits[i]
            digits[i] = (num+carry)%10
            carry=(num+carry)//10
            i=i-1

        if(carry!=0):
            digits.insert(0, carry)

        return digits

        