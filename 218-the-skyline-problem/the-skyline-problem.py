import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # 1. Collect all start and end events
        events = []
        for left, right, height in buildings:
            # Start event: use negative height so sorting prioritizes taller buildings
            events.append((left, -height))
            # End event: use positive height
            events.append((right, height))
            
        # 2. Sort events by x-coordinate, then by height impact
        events.sort()
        
        # Max-heap to track active heights (store as negative numbers for min-heap utility)
        # Initialize with 0 to represent the ground level
        max_heap = [0]
        
        # Hash map for lazy deletion of heights that have ended
        # tracks {height: count_of_active_buildings_with_this_height}
        past_heights = {}
        
        res = []
        prev_max = 0
        
        # 3. Process events sequentially
        for x, h in events:
            if h < 0:
                # Start event: add building height to heap (negated for max-heap logic)
                heapq.heappush(max_heap, h)
            else:
                # End event: register the building height as expired
                past_heights[-h] = past_heights.get(-h, 0) + 1
            
            # Lazy cleanup: remove expired heights from the top of the heap
            while max_heap[0] in past_heights and past_heights[max_heap[0]] > 0:
                past_heights[max_heap[0]] -= 1
                heapq.heappop(max_heap)
                
            # Current maximum active height
            curr_max = -max_heap[0]
            
            # 4. If the maximum height changes, we found a skyline contour key point
            if curr_max != prev_max:
                res.append([x, curr_max])
                prev_max = curr_max
                
        return res
