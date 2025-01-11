class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        size = len(s)
        start=0
        end=size-1
        
        while(start<end):
            s[start],s[end] = s[end],s[start]
            start=start+1
            end=end-1
        