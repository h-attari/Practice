class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        # split s by ' ' to create a list
        s = s.split()
        # if the length of p and s are different, they cannot match
        if len(p)!=len(s): return False
        
        # Two hash maps
        # s2p for mapping words in s to char in p
        # p2s for mapping char in p to words in p
        p2s, s2p = {}, {}
        
        for i in range(len(s)):
            
            # Add s[i] in s2p to map to p[i], if we haven't seen it before.
            if s[i] not in s2p:
                s2p[s[i]] = p[i]
            # if s[i] is already in s2p, but its value is not p[i]
            # This means there are two different char in p matched to the same word in s, so return False
            elif s2p[s[i]] != p[i]:
                return False
            
            # Same as above just from p to s.
            if p[i] not in p2s:
                p2s[p[i]] = s[i]
            elif p2s[p[i]] != s[i]:
                return False
        
        # Everything matched, return True
        return True