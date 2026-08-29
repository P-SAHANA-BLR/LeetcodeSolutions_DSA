# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
            
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Check if it's a palindrome
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed second half
        
        is_palin = True
        while second_half:  # Only need to check the second half length
            if first_half.val != second_half.val:
                is_palin = False
                break
            first_half = first_half.next
            second_half = second_half.next
            
        return is_palin
