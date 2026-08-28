class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        
        for ch_s, ch_t in zip(s, t):
            # Check mapping from s -> t
            if ch_s in map_s_to_t:
                if map_s_to_t[ch_s] != ch_t:
                    return False
            else:
                map_s_to_t[ch_s] = ch_t
                
            # Check mapping from t -> s
            if ch_t in map_t_to_s:
                if map_t_to_s[ch_t] != ch_s:
                    return False
            else:
                map_t_to_s[ch_t] = ch_s
                
        return True
