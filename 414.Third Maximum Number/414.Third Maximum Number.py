class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        size=len(nums)
        
        if(size==1):
            return nums[0]
        elif(size==2):
            if(nums[0]>nums[1]):
                return nums[0]
            else:
                return nums[1]
        
        firstMax=nums[0]
        secondMax=None
        thirdMax=None
        
        for i in range(1,size):
            if(nums[i]>firstMax):
                thirdMax=secondMax
                secondMax=firstMax
                firstMax=nums[i]
            elif((secondMax is None and nums[i]!=firstMax) or (secondMax is not None and nums[i]>secondMax and nums[i]!=firstMax)):
                thirdMax=secondMax
                secondMax=nums[i]
            elif((thirdMax is None and nums[i]!=firstMax and nums[i]!=secondMax) or (thirdMax is not None and nums[i]>thirdMax and nums[i]!=firstMax and nums[i]!=secondMax)):
                thirdMax=nums[i]
        
        if(secondMax is None or thirdMax is None):
            return firstMax
        else:
            return thirdMax