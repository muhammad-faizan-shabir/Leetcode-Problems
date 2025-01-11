class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry=0
        size1=len(num1)
        size2=len(num2)
        sum=""
        i=size1-1
        j=size2-1

        while(i>=0 and j>=0):
            sum =str((carry+int(num1[i]) + int(num2[j]))%10) + sum
            carry= (carry+int(num1[i]) + int(num2[j]))//10
            i=i-1
            j=j-1
        
        while(i>=0):
            sum=str((carry + int(num1[i]))%10)+ sum
            carry= (carry+int(num1[i]))//10
            i=i-1
        
        while(j>=0):
            sum=str((carry + int(num2[j]))%10)+ sum
            carry= (carry+int(num2[j]))//10
            j=j-1
        
        if(carry>0):
            sum=str(carry) + sum
        
        return sum