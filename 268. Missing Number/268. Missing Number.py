class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        size=len(nums)
        sum1=(size/2.0)*(size+1)
        sum2=0
        
        for i in range(0,size):
            sum2=sum2 + nums[i]
        
        missingNumber=sum1-sum2

        return int(missingNumber)
        