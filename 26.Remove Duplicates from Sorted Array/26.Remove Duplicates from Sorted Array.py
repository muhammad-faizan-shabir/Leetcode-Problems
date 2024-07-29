class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listLength= len(nums)
        if(listLength==1):
            return 1
        
        ptr1=0
        ptr2=1

        while(ptr2<listLength):
            if(nums[ptr1]==nums[ptr2]):
                nums[ptr2]=None
                ptr2=ptr2+1
            else:
                ptr1,ptr2=ptr2,ptr2+1
        
        emptyIndex=0
        currentIndex=0

        while(currentIndex<listLength):
            if(nums[currentIndex] is not None):
                if(emptyIndex!=currentIndex):
                    nums[emptyIndex]=nums[currentIndex]
                    nums[currentIndex]=None
                emptyIndex=emptyIndex+1
                currentIndex=currentIndex+1
            else:
                currentIndex=currentIndex+1
        
        k=0
        
        while(k<listLength and nums[k] is not None):
            k=k+1
        
        return k
        