from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        def bfs(src: str, dst: str) -> float:
            # If either variable is completely unseen, division cannot be determined
            if src not in graph or dst not in graph:
                return -1.0
            # A variable divided by itself is always 1.0
            if src == dst:
                return 1.0
                
            queue = deque([(src, 1.0)])
            visited = {src}
            
            while queue:
                node, current_product = queue.popleft()
                
                if node == dst:
                    return current_product
                    
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_product * weight))
                        
            return -1.0

        # 2. Process each query
        return [bfs(c, d) for c, d in queries]
