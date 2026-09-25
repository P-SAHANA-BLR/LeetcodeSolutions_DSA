class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Stack elements will store tuples of: (previous_groups_in_union, current_concatenation_group)
        stack = []
        
        # groups: stores sets that are separated by commas at the current nesting level
        groups = [] 
        # current: stores the set currently being formed by concatenation (starts as a singleton containing "")
        current = {""}
        
        for char in expression:
            if char == '{':
                # Save the current state to the stack and start a fresh context
                stack.append((groups, current))
                groups, current = [], {""}
                
            elif char == ',':
                # The current concatenation block is finished; add it to the union list
                groups.append(current)
                current = {""}
                
            elif char == '}':
                # Add the final concatenation block of the inner level to the union list
                groups.append(current)
                # Combine all sets in the union list into a single set
                inner_combined = set().union(*groups)
                
                # Pop the outer parent context from the stack
                prev_groups, prev_current = stack.pop()
                
                # Concatenate the combined inner set onto the parent's current concatenation set
                current = {p + i for p in prev_current for i in inner_combined}
                groups = prev_groups
                
            else:
                # For lowercase letters, concatenate it onto every string in the current set
                current = {s + char for s in current}
                
        # Combine any remaining groups separated by commas at the top level
        groups.append(current)
        final_set = set().union(*groups)
        
        # Return the unique words sorted alphabetically
        return sorted(list(final_set))

