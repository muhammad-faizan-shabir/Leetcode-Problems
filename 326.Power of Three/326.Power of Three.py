class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        
        noRemainder=True
        while(n>1 and noRemainder==True):
            remainder=n%3
            n=n//3
            if(remainder!=0):
                noRemainder=False

        if(noRemainder==True):
            return True
        else:
            return False    