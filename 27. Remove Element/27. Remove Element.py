class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        listLength= len(nums)

        if(listLength==0):
            return 0
        k= listLength
        for i in range(0,listLength):
            if(nums[i]==val):
                nums[i]=None
                k=k-1
        
        emptyIndex=0
        currentIndex=0

        while(currentIndex<listLength):
            if(nums[currentIndex] is not None):
                if(currentIndex!=emptyIndex):
                    nums[emptyIndex]= nums[currentIndex]
                    nums[currentIndex]=None
                currentIndex= currentIndex+1
                emptyIndex= emptyIndex+1
            else:
                currentIndex=currentIndex+1
        
        return k
        