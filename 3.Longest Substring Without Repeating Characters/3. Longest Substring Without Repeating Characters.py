class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==0 or len(s)==1):
            return len(s)

        def giveValidLength(s,i):
            strLength= len(s)
            dictionary= defaultdict(lambda: 0)
            for j in range(i,strLength):
                dictionary[s[j]]= dictionary[s[j]] +1
                
                if dictionary[s[j]]>1:
                    return j-i
            return strLength-i
        
        longestLength=1
        strLength=len(s)
        for i in range(0,strLength):
            validLength=giveValidLength(s,i)
            if(validLength>longestLength):
                longestLength=validLength
        
        return longestLength


        


        