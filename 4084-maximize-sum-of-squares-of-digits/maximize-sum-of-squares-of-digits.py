class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        # If the required sum is impossible to achieve with the given number of digits
        if sum_val > 9 * num or sum_val < 1:
            return ""
        
        # To maximize the sum of squares, we greedily take as many 9s as possible
        num_nines = sum_val // 9
        remainder = sum_val % 9
        
        # Count how many 0s are needed to fill the rest of the length
        num_zeros = num - num_nines - (1 if remainder > 0 else 0)
        
        # Construct the parts of the number
        ans = []
        ans.append("9" * num_nines)
        if remainder > 0:
            ans.append(str(remainder))
        ans.append("0" * num_zeros)
        
        # Since it's already structured from largest to smallest digits,
        # the first digit is guaranteed to be >= 1.
        return "".join(ans)
