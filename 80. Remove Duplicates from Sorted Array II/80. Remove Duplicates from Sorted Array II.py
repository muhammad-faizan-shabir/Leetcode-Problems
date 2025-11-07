class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ptr1 = 0
        ptr2 = 1
        toBeRemoved = None
        
        while(ptr2 < len(nums)):
            if(nums[ptr1] == toBeRemoved):
                nums.pop(ptr1)
            elif(nums[ptr1] == nums[ptr2]):
                toBeRemoved = nums[ptr1]
                ptr1 = ptr1 + 2
                ptr2 = ptr2 + 2
            else:
                ptr1 = ptr1 + 1
                ptr2 = ptr2 + 1
        
        if(ptr1 < len(nums) and nums[ptr1] == toBeRemoved):
            nums.pop(ptr1)
        
        return len(nums)