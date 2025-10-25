import heapq
from typing import List

class Pair:
    def __init__(self, node, time):
        self.node = node
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for src, dst, wt in times:
            adj[src].append(Pair(dst, wt))
        
        # Initialize distances
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        # Priority queue: (time, node)
        heap = [(0, k)]
        
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for neighbor in adj[node]:
                adjNode, edgeWeight = neighbor.node, neighbor.time
                if dist[node] + edgeWeight < dist[adjNode]:
                    dist[adjNode] = dist[node] + edgeWeight
                    heapq.heappush(heap, (dist[adjNode], adjNode))
        
        maxTime = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            maxTime = max(maxTime, dist[i])
        return maxTime
