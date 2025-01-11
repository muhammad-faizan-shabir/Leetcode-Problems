class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start =1
        end=num
        found=False
        
        while(start<=end and found==False):
            mid=(start +end)//2
            square=mid*mid
            if((square)==num):
                found=True
            elif(square>num):
                end=mid-1
            else:
                start=mid+1
        
        return found