class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictionary={}
        
        magazineSize=len(magazine)
        for i in range(0,magazineSize):
            dictionary[magazine[i]]= dictionary.get(magazine[i],0)+1
        
        ransomNoteSize=len(ransomNote)
        for i in range(0,ransomNoteSize):
            if((ransomNote[i] not in dictionary) or dictionary[ransomNote[i]]==0):
                return False
            else:
                dictionary[ransomNote[i]]= dictionary[ransomNote[i]]-1
        
        return True