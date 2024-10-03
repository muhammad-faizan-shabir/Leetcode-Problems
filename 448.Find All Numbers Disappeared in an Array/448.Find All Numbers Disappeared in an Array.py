class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size=len(nums)
        disappearedNum=[]
        
        for i in range(0,size):
            if(nums[abs(nums[i])-1] >0):
                nums[abs(nums[i])-1]=nums[abs(nums[i])-1]*-1
        
        for i in range(0,size):
            if(nums[i]> 0):
                disappearedNum.append(i+1)
        
        return disappearedNum        