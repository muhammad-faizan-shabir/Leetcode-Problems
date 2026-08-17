class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)

        if(size == 0):
            return
        
        zeroPtr = 0

        while(zeroPtr < size and nums[zeroPtr] != 0):
            zeroPtr = zeroPtr + 1

        nonZeroPtr = zeroPtr + 1
        
        while(nonZeroPtr < size and nums[nonZeroPtr] == 0):
            nonZeroPtr = nonZeroPtr + 1

        while(nonZeroPtr < size):
            if(nums[nonZeroPtr] != 0):
                nums[zeroPtr] = nums[nonZeroPtr]
                nums[nonZeroPtr] = 0
                zeroPtr = zeroPtr + 1
            
            nonZeroPtr = nonZeroPtr + 1