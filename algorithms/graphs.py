# Graphs are a collection of nodes (vertices) connected by edges. They can be directed or undirected, weighted or unweighted.
#
# Common representations:
# - Adjacency list: A dictionary where each node maps to a list of its neighbors.
# - Adjacency matrix: A 2D array where cell (i, j) represents an edge between nodes i and j.
#
# Common algorithms:
# - Depth-First Search (DFS)
# - Breadth-First Search (BFS)
# - Dijkstra's algorithm (shortest path)
# - Kruskal's algorithm (minimum spanning tree)

from collections import defaultdict, deque
import heapq
from typing import List, Tuple

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight=None):
        """
        Add an edge from node u to node v.
        If the graph is weighted, include a weight.
        """
        if weight is not None:
            self.graph[u].append((v, weight))
        else:
            self.graph[u].append(v)

    # ====================== Depth-First Search (DFS) ======================
    def dfs(self, start):
        """
        Perform Depth-First Search (DFS) starting from the given node.
        Returns a set of visited nodes.
        Time Complexity: O(V + E)
        """
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    stack.append(neighbor[0] if isinstance(neighbor, tuple) else neighbor)
        return visited

    # ====================== Breadth-First Search (BFS) ======================
    def bfs(self, start):
        """
        Perform Breadth-First Search (BFS) starting from the given node.
        Returns a set of visited nodes.
        Time Complexity: O(V + E)
        """
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    queue.append(neighbor[0] if isinstance(neighbor, tuple) else neighbor)
        return visited

    # ====================== Dijkstra's Algorithm ======================
    def dijkstra(self, start):
        """
        Find the shortest path from the start node to all other nodes using Dijkstra's algorithm.
        Returns a dictionary of shortest distances.
        Time Complexity: O((V + E) log V) with a priority queue.
        """
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # Skip if we've already found a better path
            if current_distance > distances[current_node]:
                continue
                
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

    # ====================== Kruskal's Algorithm ======================
    def kruskal(self):
        """
        Find the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm.
        Returns a list of edges in the MST.
        Time Complexity: O(E log E) due to sorting.
        """
        parent = {}
        def find(node):
            """
            Find the root of the set containing the given node.
            """
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u, v):
            """
            Union the sets containing u and v.
            """
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u
        
        # Initialize parent pointers
        for node in self.graph:
            parent[node] = node
        
        # Extract all edges and sort by weight
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                edges.append((weight, u, v))
        edges.sort()
        
        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))
        
        return mst
