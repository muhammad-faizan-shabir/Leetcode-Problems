class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        oneBitCount=0
        keepMoving=True
        
        while(keepMoving==True and n>0):
            if((n & 1) ==1):
                oneBitCount=oneBitCount+1
                if(oneBitCount>1):
                    keepMoving=False
            n=n>>1
        
        if(oneBitCount!=1):
            return False
        else:
            return True
        