from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_matches(pattern: str) -> List[int]:
            """
            Computes matching indices using the KMP string matching algorithm.
            """
            if not pattern or len(pattern) > len(s):
                return []
            
            # Construct the partial match table (LPS array)
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            
            # Match the pattern against text string s
            matches = []
            s_idx = 0
            p_idx = 0
            while s_idx < len(s):
                if s[s_idx] == pattern[p_idx]:
                    s_idx += 1
                    p_idx += 1
                    
                    if p_idx == len(pattern):
                        matches.append(s_idx - p_idx)
                        p_idx = lps[p_idx - 1]
                else:
                    if p_idx != 0:
                        p_idx = lps[p_idx - 1]
                    else:
                        s_idx += 1
            return matches

        # 1. Find all matching positions for both substrings in linear time
        indices_a = get_matches(a)
        indices_b = get_matches(b)
        
        if not indices_a or not indices_b:
            return []
            
        ans = []
        j = 0
        len_b = len(indices_b)
        
        # 2. Match pairs using a strict linear O(N) Two-Pointer sweep
        for i in indices_a:
            # Advance j pointer until indices_b[j] is within bounds or ahead of i - k
            while j < len_b and indices_b[j] < i - k:
                j += 1
                
            # If the current index satisfies the upper boundary condition, it is beautiful
            if j < len_b and indices_b[j] <= i + k:
                ans.append(i)
                
        return ans

