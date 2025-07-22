class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        firstThreeNums = [nums[0], nums[1], nums[2]]
        firstThreeNums.sort()
        
        firstLargestNum = firstThreeNums[2]
        secondLargestNum = firstThreeNums[1]
        thirdLargestNum = firstThreeNums[0]

        firstSmallestNum = firstThreeNums[0]
        secondSmallestNum = firstThreeNums[1]

        for i in range(3,len(nums)):
            if(nums[i] > firstLargestNum):
                thirdLargestNum = secondLargestNum
                secondLargestNum = firstLargestNum
                firstLargestNum = nums[i]
            elif(nums[i] > secondLargestNum):
                thirdLargestNum = secondLargestNum
                secondLargestNum = nums[i]
            elif(nums[i] > thirdLargestNum):
                thirdLargestNum = nums[i]
            
            if(nums[i] < firstSmallestNum):
                secondSmallestNum = firstSmallestNum
                firstSmallestNum = nums[i]
            elif(nums[i] < secondSmallestNum):
                secondSmallestNum = nums[i]
        
        return max(firstLargestNum * secondLargestNum * thirdLargestNum, firstSmallestNum * secondSmallestNum * firstLargestNum)