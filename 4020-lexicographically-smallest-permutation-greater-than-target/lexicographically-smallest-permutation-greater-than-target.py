from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        # prefix_counts[i] stores the available pool of characters 
        # after matching target perfectly from index 0 up to index i-1
        prefix_counts = [None] * (n + 1)
        prefix_counts[0] = s_counts.copy()
        
        # Step 1: Match target character-by-character from left to right
        max_prefix_len = 0
        for i in range(n):
            curr_char = target[i]
            if prefix_counts[i][curr_char] > 0:
                next_count = prefix_counts[i].copy()
                next_count[curr_char] -= 1  # Corrected consumption decrement
                prefix_counts[i + 1] = next_count
                max_prefix_len += 1
            else:
                # Character not available; cannot match any further prefix
                break
                
        # Step 2: Traverse backwards from longest matched prefix to find pivot
        for i in range(max_prefix_len, -1, -1):
            if i == n:
                # Perfect match string cannot be strictly greater, keep backtracking
                continue
                
            available = prefix_counts[i]
            target_char = target[i]
            
            # Find the smallest available character strictly greater than target[i]
            chosen_char = None
            for alpha in range(ord(target_char) + 1, ord('z') + 1):
                char = chr(alpha)
                if available[char] > 0:
                    chosen_char = char
                    break
            
            # If found, this index 'i' is our pivot point
            if chosen_char:
                result_prefix = target[:i] + chosen_char
                
                final_pool = available.copy()
                final_pool[chosen_char] -= 1
                
                # Append the rest of the pool in lexicographically sorted order
                remaining_chars = []
                for alpha in range(ord('a'), ord('z') + 1):
                    char = chr(alpha)
                    if final_pool[char] > 0:
                        remaining_chars.append(char * final_pool[char])
                        
                return result_prefix + "".join(remaining_chars)
                
        return ""
