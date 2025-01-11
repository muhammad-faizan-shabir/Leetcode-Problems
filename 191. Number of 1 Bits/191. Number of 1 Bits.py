class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        oneCount=0

        while(n>0):
            lsb= n&1
            if(lsb==1):
                oneCount=oneCount+1
            n=n>>1
        
        return oneCount

        