class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # dict. is the best way in order to take advantage of "in" and index
        res = numerals[s[len(s)-1]]
        # I want to start with the last number in case the input is only one roman  
        # numeral long or in case the numeral before it is of lesser integer value
        for char in range(len(s)-2,-1,-1): 
            # going backwards will make sure that I do miss the edge cases where a  
            # preceeding number decrements the number in front of it
            if numerals[s[char]] >= numerals[s[char+1]]:
                res += numerals[s[char]]
            else:
                res -= numerals[s[char]]
        return res