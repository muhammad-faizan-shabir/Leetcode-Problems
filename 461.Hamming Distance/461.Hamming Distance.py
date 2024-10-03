class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        xorResult=x^y
        oneCount=0

        while(xorResult>0):
            lsb=xorResult&1
            xorResult=xorResult>>1
            if(lsb==1):
                oneCount=oneCount+1
        
        return oneCount