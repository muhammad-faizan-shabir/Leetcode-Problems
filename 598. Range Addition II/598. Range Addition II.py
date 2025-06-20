class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        
        if(len(ops) == 0):
            return m * n

        minRow = None
        minCol = None
        
        for op in ops:
            if(minRow is None):
                minRow = op[0]
            elif(op[0] < minRow):
                minRow = op[0]
            
            if(minCol is None):
                minCol = op[1]
            elif(op[1] < minCol):
                minCol = op[1]
        
        return minRow * minCol