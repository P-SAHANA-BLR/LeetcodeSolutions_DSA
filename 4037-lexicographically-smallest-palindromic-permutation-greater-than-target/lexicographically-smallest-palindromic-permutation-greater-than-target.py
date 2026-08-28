from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # 1. Count character frequencies
        counts = Counter(s)
        
        # 2. Check if a palindromic permutation is possible
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
            
        mid_char = odd_chars[0] if odd_chars else ""
        
        # 3. Collect available characters for the first half
        half_chars = []
        for ch, cnt in counts.items():
            half_chars.extend([ch] * (cnt // 2))
        half_chars.sort()
        
        # 4. Greedy backtracking/construction to find the next permutation
        # We need to find a first half that makes the full palindrome > target
        ans_half = []
        
        def build(idx: int, is_greater: bool) -> bool:
            if idx == half_len:
                if is_greater:
                    return True
                # If the first half is identical to target's first half,
                # check if the full reconstructed palindrome is strictly greater.
                full_pal = "".join(ans_half) + mid_char + "".join(reversed(ans_half))
                return full_pal > target
            
            # Determine the range of characters we can place at position `idx`
            unique_choices = sorted(list(set(half_chars)))
            
            for ch in unique_choices:
                # If we haven't broken out to be greater yet, we cannot pick a smaller character
                if not is_greater and ch < target[idx]:
                    continue
                    
                # Try placing `ch`
                half_chars.remove(ch)
                ans_half.append(ch)
                
                next_greater = is_greater or (ch > target[idx])
                
                # Optimization: If it's already greater, the best choice is to fill 
                # the remaining positions with the absolute smallest characters remaining.
                if next_greater:
                    # remaining characters are already sorted in `half_chars`
                    final_half = ans_half + half_chars
                    full_pal = "".join(final_half) + mid_char + "".join(reversed(final_half))
                    if full_pal > target:
                        ans_half.extend(half_chars)
                        return True
                else:
                    # If it's equal to target[idx], recurse to check deeper positions
                    if build(idx + 1, next_greater):
                        return True
                
                # Backtrack
                ans_half.pop()
                half_chars.append(ch)
                half_chars.sort()
                
            return False

        if build(0, False):
            return "".join(ans_half) + mid_char + "".join(reversed(ans_half))
        
        return ""
