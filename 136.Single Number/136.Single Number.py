class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        size=len(nums)
        number=0

        for i in range(0,size):
            number= number^nums[i]
        
        return number