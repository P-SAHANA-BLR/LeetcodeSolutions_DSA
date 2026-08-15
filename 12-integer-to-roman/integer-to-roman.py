class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to their Roman numeral representations in descending order
        # Subtractive edge cases (4, 9, 40, 90, 400, 900) are hardcoded directly
        mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = []
        
        # Iterating through values greedily constructs the string at maximum speed
        for value, symbol in mapping:
            if num == 0:
                break
            # Determine how many times this specific Roman character fits
            count = num // value
            if count:
                res.append(symbol * count)
                num %= value
                
        return "".join(res)
