class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        
        if n==1:
            return [0,1]
        
        listOfOneCount=[0,1]

        for i in range(2,n+1):
            if(i%2==0):
                listOfOneCount.append(listOfOneCount[i//2])
            else:
                listOfOneCount.append(1+listOfOneCount[i//2])
        
        return listOfOneCount