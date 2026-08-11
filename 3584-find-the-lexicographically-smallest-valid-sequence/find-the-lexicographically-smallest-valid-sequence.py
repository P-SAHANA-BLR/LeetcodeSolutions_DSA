class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # last_match[i] stores the index in word2 up to which the suffix word1[i:] 
        # can match greedily without any modifications.
        last_match = [-1] * (n + 1)
        
        # Fill last_match from right to left
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            last_match[i] = j + 1
            
        ans = []
        j = 0  # pointer for word2
        modified = False  # tracker for our 1-character modification budget
        
        # Match from left to right greedily
        for i in range(n):
            if j == m:
                break
                
            # Case 1: Exact character match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Case 2: Mismatch, but we can consume our single modification here
            elif not modified:
                # Check if the remaining suffix of word1 can cover the rest of word2
                if last_match[i + 1] <= j + 1:
                    ans.append(i)
                    j += 1
                    modified = True
                    
        return ans if len(ans) == m else []
