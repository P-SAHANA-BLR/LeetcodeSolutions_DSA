class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find the first and last occurrence of each character
        first = {c: i for i, c in enumerate(s)}
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in first or i < first[c]:
                first[c] = i
        
        # Build the exact first/last positions correctly
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        valid_intervals = []

        # Step 2: Extend intervals for each unique character
        for c in first:
            start = first[c]
            end = last[c]
            
            i = start
            is_valid = True
            while i <= end:
                # Expand boundaries based on characters seen inside
                char_start = first[s[i]]
                char_end = last[s[i]]
                
                # If a character inside started before our 'start', this interval
                # is a duplicate or subset of a larger one we will process later.
                if char_start < start:
                    is_valid = False
                    break
                
                end = max(end, char_end)
                i += 1
                
            if is_valid:
                valid_intervals.append((start, end))

        # Step 3: Greedy selection (Interval Scheduling)
        # Sort primarily by end position to pick the earliest ending intervals
        valid_intervals.sort(key=lambda x: x[1])
        
        result = []
        prev_end = -1
        
        for start, end in valid_intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end
                
        return result
