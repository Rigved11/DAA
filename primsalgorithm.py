import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Representation: Adjacency list where self.adj[u] stores tuples of (v, weight)
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        # Prim's algorithm typically works on undirected graphs
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def prim_mst(self, start_vertex=0):
        # Track if a vertex is already included in the MST
        in_mst = [False] * self.V
        
        # Track the parent of each vertex to reconstruct the tree structure
        parent = [-1] * self.V
        
        # Track the minimum edge weight connection cost to the MST
        key = [float('inf')] * self.V
        
        # Min-Heap stores elements as tuples: (weight, vertex)
        # It prioritizes extracting the vertex with the smallest incoming edge weight
        min_heap = []

        # Step 1: Initialize the starting vertex
        key[start_vertex] = 0
        heapq.heappush(min_heap, (0, start_vertex))

        mst_edges = []
        total_weight = 0

        # Step 2: Loop until the heap is empty
        while min_heap:
            # Extract the vertex with the minimum edge weight connection
            weight, u = heapq.heappop(min_heap)

            # Skip processing if the vertex is already part of the MST
            if in_mst[u]:
                continue

            # Include the vertex in the MST
            in_mst[u] = True
            total_weight += weight
            
            # If it's not the starting vertex, record the edge
            if parent[u] != -1:
                mst_edges.append((parent[u], u, weight))

            # Step 3: Update key values and parent index of adjacent vertices
            for v, edge_weight in self.adj[u]:
                # If v is not yet in MST and the new edge is cheaper than its current key
                if not in_mst[v] and edge_weight < key[v]:
                    key[v] = edge_weight
                    parent[v] = u
                    heapq.heappush(min_heap, (edge_weight, v))

        return mst_edges, total_weight


# --- Driver Code Example ---
if __name__ == "__main__":
    # Create a graph with 4 vertices (0, 1, 2, 3)
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    # Run Prim's Algorithm starting from vertex 0
    mst_edges, total_cost = g.prim_mst(start_vertex=0)

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == Weight: {weight}")
    print(f"Total Weight of MST: {total_cost}")
