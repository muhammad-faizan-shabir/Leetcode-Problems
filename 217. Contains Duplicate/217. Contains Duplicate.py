class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dictionary={}
        size=len(nums)
        
        for i in range(0,size):
            dictionary[nums[i]]=dictionary.get(nums[i],0)+1
            
        containsDuplicate=False
        
        for i in dictionary:
            if(dictionary[i]>=2):
                containsDuplicate=True
        
        return containsDuplicate
            