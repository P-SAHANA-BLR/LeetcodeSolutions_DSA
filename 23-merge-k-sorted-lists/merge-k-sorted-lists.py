import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Dummy head simplifies list construction mechanics
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        # Push the head of each non-empty linked list into the min-heap
        # We include an incrementing index `i` to avoid direct comparison 
        # between ListNode objects if they share duplicate values.
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
                
        # Extract the minimum node from the heap and append its next element
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # If the popped node has a next element, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
