class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        i=0
        maxOnes=0

        while(i<size):
            tempOnes=0
            
            while(i<size and nums[i]!=0):
                tempOnes=tempOnes+1
                i=i+1
            
            if(tempOnes>maxOnes):
                maxOnes=tempOnes
            i=i+1
        
        return maxOnes