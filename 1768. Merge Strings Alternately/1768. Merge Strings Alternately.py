class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedStr = ""
        len1 = len(word1)
        len2 = len(word2)
        i = 0

        while(i < len1 and i < len2):
            mergedStr = mergedStr + word1[i] + word2[i]
            i = i + 1
        
        if(i < len1):
            mergedStr = mergedStr + word1[i:len1]
        
        if(i < len2):
            mergedStr = mergedStr + word2[i:len2]

        return mergedStr