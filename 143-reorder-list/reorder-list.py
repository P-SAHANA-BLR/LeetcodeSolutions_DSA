# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow is now at the middle. Split the list into two halves.
        second = slow.next
        slow.next = None  # Disconnect the first half from the second half
        
        # Step 2: Reverse the second half
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # prev now points to the head of the reversed second half
        first, second = head, prev
        
        # Step 3: Merge the two halves alternately
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
