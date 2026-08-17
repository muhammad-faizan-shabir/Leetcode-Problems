class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        size = len(candies)
        
        if(size == 0):
            return []
        
        greatest = candies[0]
        
        for i in range(1,size):
            greatest = max(greatest,candies[i])

        result = []
        
        for i in range(size):
            if(candies[i] + extraCandies >= greatest):
                result.append(True)
            else:
                result.append(False)
        
        return result