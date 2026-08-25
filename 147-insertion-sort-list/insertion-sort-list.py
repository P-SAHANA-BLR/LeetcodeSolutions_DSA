# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        
        while curr and curr.next:
            # Optimization: If the next node is already in the right position, skip insertion scan
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                # Find the node to insert
                to_insert = curr.next
                # Sever it from the list
                curr.next = to_insert.next
                
                # Locate insertion position from the beginning of the sorted portion
                prev = dummy
                while prev.next.val < to_insert.val:
                    prev = prev.next
                    
                # Insert the node
                to_insert.next = prev.next
                prev.next = to_insert
                
        return dummy.next
