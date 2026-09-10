# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers to the head
        slow = head
        fast = head
        
        # Move fast by 2 steps and slow by 1 step. 
        # We must check both 'fast' and 'fast.next' to avoid AttributeError.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, a cycle exists
            if slow == fast:
                return True
                
        # If fast reaches the end, there is no cycle
        return False
