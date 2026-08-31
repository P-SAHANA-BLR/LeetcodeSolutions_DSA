# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        min_dist = float('inf')
        max_dist = -1
        
        first_cp_index = -1
        prev_cp_index = -1
        
        # Track positions using a 1-based index matching the example logic
        curr_index = 1 
        
        prev = head
        curr = head.next
        
        while curr.next:
            nxt = curr.next
            
            # Check if current node is a local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_cp_index == -1:
                    # First critical point encountered
                    first_cp_index = curr_index
                else:
                    # Subsequent critical points encountered
                    min_dist = min(min_dist, curr_index - prev_cp_index)
                    max_dist = curr_index - first_cp_index
                
                # Update the previous critical point index to the current one
                prev_cp_index = curr_index
            
            # Move pointers forward
            prev = curr
            curr = nxt
            curr_index += 1
            
        # If fewer than two critical points were found, return [-1, -1]
        if max_dist == -1:
            return [-1, -1]
            
        return [min_dist, max_dist]
