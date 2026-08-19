class Solution:
    def toHex(self, num: int) -> str:
        
        # Edge case for zero
        if num == 0:
            return "0"
            
        # Hexadecimal character mapping
        hex_map = "0123456789abcdef"
        
        # Convert negative numbers to 32-bit unsigned equivalent (two's complement)
        if num < 0:
            num &= 0xFFFFFFFF
            
        result = []
        
        # Process the number 4 bits at a time
        while num > 0:
            # Extract the last 4 bits (values 0-15)
            digit = num & 15
            result.append(hex_map[digit])
            # Right shift by 4 bits to process the next digit
            num >>= 4
            
        # Since we collected digits from right to left, reverse the result
        return "".join(reversed(result))
