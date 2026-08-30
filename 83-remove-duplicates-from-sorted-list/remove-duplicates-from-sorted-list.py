# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list or single-node list
        if not head:
            return head
            
        current = head
        
        # Traverse the list until the end
        while current and current.next:
            if current.val == current.next.val:
                # Bypass the duplicate node
                current.next = current.next.next
            else:
                # Advance pointer only if no duplicate was deleted
                current = current.next
                
        return head
