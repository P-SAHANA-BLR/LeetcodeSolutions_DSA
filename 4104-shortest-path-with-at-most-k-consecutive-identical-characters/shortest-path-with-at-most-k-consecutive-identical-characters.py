import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Priority queue stores tuples of: (weight, current_node, last_char, consecutive_count)
        # We represent characters as their ASCII integer index (0-25) to map easily to arrays/dicts
        start_char = ord(labels[0]) - ord('a')
        
        # min-heap initialization
        pq = [(0, 0, start_char, 1)]
        
        # dist tracking: dist[node] = maps (last_char, consecutive_count) -> minimum weight
        # Using a list of dictionaries to handle the sparse nature of states efficiently
        visited_states = [{} for _ in range(n)]
        visited_states[0][(start_char, 1)] = 0
        
        while pq:
            w, u, last_char, count = heapq.heappop(pq)
            
            # If we reached the destination node, since it's a min-heap, this is the shortest valid path
            if u == n - 1:
                return w
                
            # If we found a strictly better path to this exact state already, skip processing
            if visited_states[u].get((last_char, count), float('inf')) < w:
                continue
                
            # Explore neighbors
            for v, weight in adj[u]:
                v_char = ord(labels[v]) - ord('a')
                
                # Calculate consecutive count for the next node
                if v_char == last_char:
                    new_count = count + 1
                else:
                    new_count = 1
                    
                # Valid transition only if it does not exceed k consecutive identical characters
                if new_count <= k:
                    new_weight = w + weight
                    state = (v_char, new_count)
                    
                    # Relaxation step
                    if new_weight < visited_states[v].get(state, float('inf')):
                        visited_states[v][state] = new_weight
                        heapq.heappush(pq, (new_weight, v, v_char, new_count))
                        
        return -1
