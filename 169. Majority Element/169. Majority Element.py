class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        size = len(nums)
        counts = {}
        
        for i in range(size):
            if(nums[i] in counts):
                counts[nums[i]] = counts[nums[i]] + 1
            else:
                counts[nums[i]] =  1
        
        threshold = size / 2

        for count in counts:
            if(counts[count] > threshold):
                majority = count
                break
        
        return majority