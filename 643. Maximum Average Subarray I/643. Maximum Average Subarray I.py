class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        currentSum = 0
        for i in range(k):
            currentSum = currentSum + nums[i]
        
        pointerOne = 0
        pointerTwo = k
        k = float(k)
        maxSum = currentSum
        
        while(pointerTwo < len(nums)):
            currentSum = currentSum - nums[pointerOne] + nums[pointerTwo]
            
            if(currentSum/k > maxSum/k):
                maxSum = currentSum
            
            pointerOne = pointerOne + 1
            pointerTwo = pointerTwo + 1

        return maxSum/k