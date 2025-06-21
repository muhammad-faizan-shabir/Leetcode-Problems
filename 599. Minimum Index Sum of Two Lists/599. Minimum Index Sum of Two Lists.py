class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        lst = []
        leastIndexSum = None

        for i in range(len(list1)):
            for j in range(len(list2)):
                if(list1[i] == list2[j]):
                    if(leastIndexSum is None):
                        leastIndexSum = i + j
                        lst = [list1[i]]
                    else:
                        if(i + j == leastIndexSum):
                            lst.append(list1[i])
                        elif(i + j < leastIndexSum):
                            leastIndexSum = i + j
                            lst = [list1[i]]
        
        return lst