class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        answer = [1] * size
        leftProduct = 1
        rightProduct = 1

        for i in range(size - 1):
            leftProduct = leftProduct * nums[i]
            answer[i + 1] = leftProduct
        
        for i in range(size - 1 , 0 ,-1):
            rightProduct = rightProduct * nums[i]
            answer[i - 1] = answer[i - 1] * rightProduct
        
        return answer