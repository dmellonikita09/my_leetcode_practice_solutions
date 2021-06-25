from collections import Counter 
class Solution:
    def canConstruct( ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        for i in r_count:
            if r_count[i] > m_count[i]:
                return False
        return True
    ransomNote = "aa"
    magazine = "ab"
    print(canConstruct(ransomNote, magazine))
