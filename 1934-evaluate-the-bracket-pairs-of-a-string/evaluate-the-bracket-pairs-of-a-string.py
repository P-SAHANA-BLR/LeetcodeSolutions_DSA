class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert the knowledge list into a hash map for O(1) lookups
        k_map = {key: val for key, val in knowledge}
        
        res = []
        is_inside_bracket = False
        current_key = []
        
        for char in s:
            if char == '(':
                is_inside_bracket = True
            elif char == ')':
                is_inside_bracket = False
                # Form the key string from the collected characters
                key_str = "".join(current_key)
                # Append the value if it exists, otherwise append "?"
                res.append(k_map.get(key_str, "?"))
                # Clear the key buffer for the next bracket pair
                current_key = []
            else:
                if is_inside_bracket:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)
