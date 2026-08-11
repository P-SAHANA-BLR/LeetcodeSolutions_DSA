import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Filter out invalid prime factors in t
        temp_t = t
        for p in (2, 3, 5, 7):
            while temp_t % p == 0:
                temp_t //= p
        if temp_t > 1:
            return "-1"
            
        n = len(num)
        
        def get_min_suffix(target: int) -> str:
            if target <= 1:
                return ""
            res = []
            for d in (9, 8, 7, 6, 5, 4, 3, 2):
                while target % d == 0:
                    res.append(str(d))
                    target //= d
            return "".join(reversed(res))

        # Track the active target remaining for valid prefixes of num
        left_t = [t] * (n + 1)
        first_zero_idx = n  # Keep track of where the first zero appears
        
        for i, ch in enumerate(num):
            d = int(ch)
            if d == 0:
                first_zero_idx = i
                break
            left_t[i + 1] = left_t[i] // math.gcd(left_t[i], d)
        else:
            # If the original string contains no zeros and satisfies t, return it
            if left_t[n] == 1:
                return num

        # Step 2: Backtrack starting ONLY from the first zero or to its left.
        # Any index to the right of a zero is invalid to mutate.
        for i in range(min(n - 1, first_zero_idx), -1, -1):
            curr_digit = 0 if i == first_zero_idx else int(num[i])
            
            # Try to increment the current digit
            for d in range(curr_digit + 1, 10):
                rem_t = left_t[i] // math.gcd(left_t[i], d)
                min_suffix = get_min_suffix(rem_t)
                
                # Check if the remaining slots can accommodate the needed factors
                rem_slots = n - 1 - i
                if len(min_suffix) <= rem_slots:
                    # Pad out the front of the suffix with '1's to make it small
                    ones_padding = "1" * (rem_slots - len(min_suffix))
                    return num[:i] + str(d) + ones_padding + min_suffix
                    
        # Step 3: If no valid mutation fits in length n, increase length to n + 1
        min_suffix = get_min_suffix(t)
        rem_slots = n + 1
        ones_padding = "1" * (rem_slots - len(min_suffix))
        return ones_padding + min_suffix
