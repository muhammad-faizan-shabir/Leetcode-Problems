class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        totalSum = 0
        
        for i in range(size):
            totalSum = totalSum + nums[i]
        
        leftSum = 0
        rightSum = 0

        for i in range(size):
            rightSum = totalSum - leftSum - nums[i]
            
            if(leftSum == rightSum):
                return i
            
            leftSum = leftSum + nums[i]
        
        return -1