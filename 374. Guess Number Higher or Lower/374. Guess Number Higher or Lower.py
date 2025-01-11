# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        end=n
        guessCorrect=False
        
        while(guessCorrect==False):
            mid = (start+end)//2
            response=guess(mid)
            if(response==0):
                guessCorrect=True
            elif(response==-1):
                end=mid-1
            else:
                start=mid+1
        
        return mid