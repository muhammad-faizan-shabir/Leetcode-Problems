class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        
        if(((n) & (n-1))==0 and (bin(n).count('0')-1) % 2 == 0):
            return True
        else:
            return False