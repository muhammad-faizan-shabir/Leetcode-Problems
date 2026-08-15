class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = {}

        for num in arr:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        occured = {}

        for frequency in frequencies.values():
            if(occured.get(frequency, False)):
                return False
            else:
                occured[frequency] = True
        
        return True