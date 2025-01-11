class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        size= len(prices)
        currentIndex=1
        minIndex=0
        maxProfit=0

        while(currentIndex<size):
            if(prices[currentIndex]-prices[minIndex]>=0):
                if(prices[currentIndex]-prices[minIndex]>maxProfit):
                    maxProfit=prices[currentIndex]-prices[minIndex]
            else:
                minIndex=currentIndex
            
            currentIndex=currentIndex+1
        
        return maxProfit






        
