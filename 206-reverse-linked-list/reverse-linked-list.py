class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
            
        # Reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Make the next node point back to the current node
        head.next.next = head
        head.next = None
        
        return new_head
