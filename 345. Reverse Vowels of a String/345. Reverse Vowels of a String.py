class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        size=len(s)
        start =0
        end=size-1
        lst=list(s)

        while(start<end):
            while(start<size and (lst[start] not in ['a','e','i','o','u','A','E','I','O','U'])):
                start=start+1

            while(end>=0 and (lst[end] not in ['a','e','i','o','u','A','E','I','O','U'])):
                end=end-1

            if(start <end):
                lst[start],lst[end]= lst[end],lst[start]
            
            start=start+1
            end=end-1
        
        s= ''.join(lst)
        return s
        