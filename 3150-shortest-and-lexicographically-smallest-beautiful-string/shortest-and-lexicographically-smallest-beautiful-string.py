class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        min_len = float('inf')
        
        left = 0
        ones_count = 0
        
        for right in range(len(s)):
            if s[right] == '1':
                ones_count += 1
                
            # Shrink the window from the left if it has exactly k ones
            while ones_count == k:
                # A valid beautiful substring candidate
                current_substring = s[left:right + 1]
                current_len = right - left + 1
                
                # Update answer if it's shorter, or same length but lexicographically smaller
                if current_len < min_len:
                    min_len = current_len
                    ans = current_substring
                elif current_len == min_len:
                    if current_substring < ans:
                        ans = current_substring
                
                # Move left pointer to look for smaller/better windows
                if s[left] == '1':
                    ones_count -= 1
                left += 1
                
        return ans
