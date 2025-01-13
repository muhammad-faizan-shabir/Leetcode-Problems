class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def getNextGreaterElement(num,nums2):
            size2 = len(nums2)
            i=0
            
            while(i< size2):
                if(num==nums2[i]):
            
                    while(i<size2):
                        if(nums2[i]>num):
                            return nums2[i]
                        else:
                            i=i+1
                else:
                    i=i+1
            
            return -1
        
        size1=len(nums1)
        ans=[]
        
        for i in range(size1):
            ans.append(getNextGreaterElement(nums1[i],nums2))
        
        return ans        