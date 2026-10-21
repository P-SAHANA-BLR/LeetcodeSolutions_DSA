class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        match_idx = 0
        star_idx = -1
        
        s_len, p_len = len(s), len(p)
        
        while s_idx < s_len:
            # Case 1: Characters match, or pattern has a '?'
            if p_idx < p_len and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
                
            # Case 2: Pattern has a '*', record the position for backtracking
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
                
            # Case 3: Current characters don't match, check if we can backtrack to the last '*'
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
                
            # Case 4: Characters don't match and there is no '*' to backtrack to
            else:
                return False
                
        # Check if remaining characters in the pattern are all '*'
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == p_len
