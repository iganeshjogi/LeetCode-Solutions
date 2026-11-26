class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_frequency = {}
        t_frequency = {}

        for i in s:
            if i in s_frequency:
                s_frequency[i] += 1
            else:
                s_frequency[i] = 1

        for i in t:
            if i in t_frequency:
                t_frequency[i] += 1
            else:
                t_frequency[i] = 1
        
        if s_frequency == t_frequency:
            return True
        
        else:
            return False

        
        