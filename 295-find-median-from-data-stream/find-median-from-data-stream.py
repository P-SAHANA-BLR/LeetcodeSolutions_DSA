import heapq

class MedianFinder:

    def __init__(self):
        # max_heap stores the smaller half of the numbers (inverted for max-heap behavior)
        self.max_heap = []
        # min_heap stores the larger half of the numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max_heap first (store inverted value)
        heapq.heappush(self.max_heap, -num)
        
        # Step 2: Ensure every element in max_heap is <= every element in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
            
        # Step 3: Maintain size property (max_heap can only have at most 1 more element than min_heap)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
