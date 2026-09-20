class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        # dp[i][j] will be True if s[i..j] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        # Precompute palindrome status for all substrings
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        
        result = []
        
        def backtrack(start: int, current_partition: list[str]):
            # If we've reached the end of the string, a valid partitioning is found
            if start == n:
                result.append(list(current_partition))
                return
            
            # Try every possible end position for the current substring
            for end in range(start, n):
                if dp[start][end]:
                    # Choose
                    current_partition.append(s[start:end + 1])
                    # Explore
                    backtrack(end + 1, current_partition)
                    # Unchoose (Backtrack)
                    current_partition.pop()
                    
        backtrack(0, [])
        return result
