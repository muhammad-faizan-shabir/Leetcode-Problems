class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        size = len(nums)
        originalSum = (size * (size+1)) / 2
        currentSum = 0
        
        for i in range(size):
            if(nums[abs(nums[i]) - 1] > 0):
                nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] * -1
            
            currentSum = currentSum + abs(nums[i])
        
        for i in range(size):
            if(nums[i] > 0):
                disappearedNum = i + 1
        
        return [disappearedNum - (originalSum - currentSum), disappearedNum]