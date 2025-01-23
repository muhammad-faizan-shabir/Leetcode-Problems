class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if(num==1):
            return False
        
        sum=1
        limit= int(sqrt(num))

        for i in range(2,limit+1):
            if(num%i==0):
                sum=sum+i+(num//i)
        
        if(sum==num):
            return True
        else:
            return False