class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dictionary={}
        size=len(nums)
        
        for i in range(size):
            if(nums[i] in dictionary and abs(i-dictionary[nums[i]])<=k):
                return True
            dictionary[nums[i]]=i
        
        return False