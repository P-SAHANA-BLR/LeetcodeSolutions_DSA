class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        first = -1
        
        # Unrolled digit tracking to completely avoid int() conversion overhead
        for d, val in (('9', 9), ('8', 8), ('7', 7), ('6', 6), ('5', 5), 
                       ('4', 4), ('3', 3), ('2', 2), ('1', 1), ('0', 0)):
            c = s.count(d)
            if c:
                if first == -1:
                    if c > 1:
                        return val * val  # Both highest digits are the same
                    first = val
                else:
                    return first * val    # Found the second highest digit
