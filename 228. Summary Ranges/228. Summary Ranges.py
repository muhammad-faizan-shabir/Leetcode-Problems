class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        sizeOfNums = len(nums)
        
        if(sizeOfNums == 0):
            return []
        
        i = 0
        lb = ub = nums[0]
        ranges = []
        
        while(i < sizeOfNums):
            if((i + 1) < sizeOfNums and nums[i + 1] != (ub + 1)):
                if(lb != ub):
                    ranges.append(str(lb) + "->" + str(ub))
                else:
                    ranges.append(str(lb))
                
                lb = ub = nums[i + 1]
            elif((i + 1) < sizeOfNums):
                ub = nums[i + 1]
            
            i = i + 1
        
        if(lb != ub):
            ranges.append(str(lb) + "->" + str(ub))
        else:
            ranges.append(str(lb))

        return ranges