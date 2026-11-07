import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # free_servers heap stores: (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # used_servers heap stores: (free_time, weight, index)
        used_servers = []
        
        ans = []
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            # The current time cannot be less than the arrival time of the j-th task
            current_time = max(current_time, j)
            
            # If no servers are free, we must fast-forward time to the next available server
            if not free_servers:
                current_time = used_servers[0][0]
                
            # Free up all servers that have finished their tasks by the current_time
            while used_servers and used_servers[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(used_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            # Assign the task to the best available free server
            weight, idx = heapq.heappop(free_servers)
            ans.append(idx)
            
            # Push the server into the used heap with its release time
            heapq.heappush(used_servers, (current_time + task_time, weight, idx))
            
        return ans
