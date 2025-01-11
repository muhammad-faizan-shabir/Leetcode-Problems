class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        completeRows= (-1+(pow(1+(8*n),0.5)))//2
        
        return int(completeRows)