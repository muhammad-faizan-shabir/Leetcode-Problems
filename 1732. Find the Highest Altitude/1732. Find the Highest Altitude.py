class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        size = len(gain)

        if(size == 0):
            return 0
        
        highestAltitude = 0
        currentAltitude = 0

        for i in range(size):
            currentAltitude = currentAltitude + gain[i]

            highestAltitude = max(highestAltitude, currentAltitude)

        return highestAltitude