class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        arrSize = len(arr)
        left = 0
        right = arrSize - 1
        closestElement = None
        closestIndex = None
        found = False
        while(found == False and left <= right):
            midIndex = (left + right) // 2
            midElement = arr[midIndex]

            if(midElement == x):
                found = True
            elif(midElement < x):
                left = midIndex + 1
            else:
                right = midIndex - 1
           
            if(closestElement is None or abs(midElement - x) < abs(closestElement - x) or (abs(midElement - x) == abs(closestElement - x) and midIndex < closestIndex)):
                closestElement = midElement
                closestIndex = midIndex
        
        closestCount = 1
        kNearestElements = [closestElement]
        left = closestIndex - 1
        right = closestIndex + 1
        while(closestCount < k and left >= 0 and right < arrSize):
            if(abs(x - arr[left]) > abs(x - arr[right])):
                kNearestElements.append(arr[right])
                right = right + 1
            else:
                kNearestElements.insert(0,arr[left])
                left = left - 1
            
            closestCount = closestCount + 1
        
        while(closestCount < k and left >= 0):
            kNearestElements.insert(0,arr[left])
            left = left - 1
            closestCount = closestCount + 1
        
        while(closestCount < k and right < arrSize):
            kNearestElements.append(arr[right])
            right = right + 1
            closestCount = closestCount + 1
        
        return kNearestElements