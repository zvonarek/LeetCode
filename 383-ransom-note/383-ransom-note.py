class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = set(ransomNote)
        for char in letters:
            if (ransomNote.count(char) >  magazine.count(char)): return False
        return True