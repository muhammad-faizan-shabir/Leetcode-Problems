class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        listLength= len(nums)
        start=0
        end=listLength-1
        found=False
        mid=None
       
        while((start<=end) and (found==False)):
            mid = (start+end)//2

            if(nums[mid]==target):
                found=True
            elif(nums[mid]>target):
                end=mid-1
            else:
                start=mid+1

        if(found==True):
            return mid
        else:
            if(nums[mid]>target):
                return mid
            else:
                return mid+1