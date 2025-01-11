class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        start=0
        end=x
        found=False
        mid=None

        while(start<=end and found==False):
            mid= (start+end)//2
            if((mid*mid)==x):
                found=True
            elif((mid*mid)>x):
                end=mid-1
            else:
                start=mid+1
        
        if(found==True):
            return mid
        elif((mid*mid)>x):
            return mid-1
        else:
            return mid
        