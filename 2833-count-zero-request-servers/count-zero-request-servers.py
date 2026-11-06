from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # 1. Sort logs chronologically by their timestamps
        logs.sort(key=lambda log: log[1])
        
        # 2. Pair each query with its original index so we can place results correctly
        # Sorted by the query time value
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        # Frequency array to count requests per server inside the sliding window
        # Size n + 1 because server IDs are 1-indexed (1 <= server_id <= n)
        server_counts = [0] * (n + 1)
        active_servers = 0  # Count of distinct servers with >= 1 request in current window
        
        ans = [0] * len(queries)
        left = 0
        right = 0
        num_logs = len(logs)
        
        # 3. Process each query using the sliding window
        for orig_idx, query_time in sorted_queries:
            start_time = query_time - x
            end_time = query_time
            
            # Expand the window from the right: Include all logs up to end_time
            while right < num_logs and logs[right][1] <= end_time:
                server_id = logs[right][0]
                if server_counts[server_id] == 0:
                    active_servers += 1
                server_counts[server_id] += 1
                right += 1
                
            # Shrink the window from the left: Exclude all logs strictly before start_time
            while left < num_logs and logs[left][1] < start_time:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # The answer is total servers minus the active servers in the current interval
            ans[orig_idx] = n - active_servers
            
        return ans

