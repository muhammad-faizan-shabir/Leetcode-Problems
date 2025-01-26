class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
        size= len(candyType)
        candiesToEat=size//2
        types={}

        for Type in candyType:
            types[Type] = types.get(Type,0) + 1
        
        numberOfTypes= len(types)

        if(numberOfTypes>candiesToEat):
            return candiesToEat
        else:
            return numberOfTypes