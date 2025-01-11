class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        sumOfSquares=0
        dictionary={}
        keepMoving=True
        
        while(keepMoving==True):
        
            sumOfSquares=0
            while(n>0):
                sumOfSquares=sumOfSquares+((n%10)*(n%10))
                n=n//10
            
            n=sumOfSquares
            dictionary[sumOfSquares]= dictionary.get(sumOfSquares,0)+1
            if(sumOfSquares==1 or dictionary[sumOfSquares]>1):
                keepMoving=False
        
        if(sumOfSquares==1):
            return True
        else:
            return False