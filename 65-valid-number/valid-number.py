class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ('+', '-'):
                # Signs can only appear at index 0 or right after an exponent 'e'/'E'
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
            elif char == '.':
                # Dot is invalid if we already saw a dot or an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in ('e', 'E'):
                # Exponent is invalid if we haven't seen a digit yet or already saw an exponent
                if not seen_digit or seen_exponent:
                    return False
                seen_exponent = True
                seen_digit = False  # Reset to ensure digits follow the exponent
            else:
                # Any other character is strictly invalid
                return False
                
        return seen_digit
