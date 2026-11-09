import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Track the number of requests handled by each server
        request_counts = [0] * k
        
        # Min-heap to track active servers: stores tuples of (free_time, server_id)
        busy = []
        
        # SortedList to store currently available server IDs
        available = SortedList(range(k))
        
        for i, (start_time, duration) in enumerate(zip(arrival, load)):
            # 1. Release all servers that have finished their jobs by the current arrival time
            while busy and busy[0][0] <= start_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            
            # If no servers are available, the request is dropped
            if not available:
                continue
            
            # 2. Find the optimal server starting from preferred index (i % k)
            preferred_id = i % k
            idx = available.bisect_left(preferred_id)
            
            # If no server ID >= preferred_id, wrap around to the smallest available ID
            if idx == len(available):
                idx = 0
                
            chosen_server = available[idx]
            
            # 3. Assign the request to the chosen server
            request_counts[chosen_server] += 1
            available.remove(chosen_server)
            heapq.heappush(busy, (start_time + duration, chosen_server))
            
        # Find the maximum requests handled by any server
        max_requests = max(request_counts)
        
        # Gather all server IDs that achieved this maximum
        return [server_id for server_id, count in enumerate(request_counts) if count == max_requests]
