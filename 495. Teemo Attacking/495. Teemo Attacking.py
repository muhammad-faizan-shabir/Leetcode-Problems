class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        size=len(timeSeries)
        seconds=duration
        
        for i in range(size-1):
            if(timeSeries[i]+duration-1 >=timeSeries[i+1]):
                seconds=seconds+(timeSeries[i+1] -timeSeries[i])
            else:
                seconds=seconds+duration
        
        return seconds