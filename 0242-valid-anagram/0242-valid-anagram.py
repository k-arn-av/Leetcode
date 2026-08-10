class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)==len(t):
            for i in range(len(s)):
                if s.count(s[i]) != t.count(s[i]):
                    return False
                
            return True
        return False
