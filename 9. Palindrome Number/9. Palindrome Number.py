class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if(x<0):
            return False
        
        if(x>=0 and x<=9):
            return True

        reverse = 0
        temp=x
        while(temp>0):
            reverse = (reverse*10) + (temp%10)
            temp=temp//10
        
        if(reverse==x):
            return True
        else:
            return False

        