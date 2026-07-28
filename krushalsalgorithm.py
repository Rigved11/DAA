class DisjointSet:
    def __init__(self, n):
        # Initially, every node is its own parent
        self.parent = list(range(n))
        # Rank tracks the depth of the trees for balanced merging
        self.rank = [0] * n

    def find(self, i):
        # Path compression: flattens the tree structure for O(1) amortized lookups
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank: attach the smaller tree under the larger tree
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True  # Union was successful (no cycle)
        return False  # Nodes were already in the same set (cycle detected)


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        # Store edges as a list of triplets: (u, v, weight)
        self.edges.append((u, v, weight))

    def kruskal_mst(self):
        mst = []
        mst_weight = 0
        
        # Step 1: Sort all edges in non-decreasing order of their weight
        self.edges.sort(key=lambda edge: edge[2])
        
        # Initialize the disjoint set for all vertices
        dsu = DisjointSet(self.V)

        # Step 2: Iterate through sorted edges
        for u, v, weight in self.edges:
            # Step 3: If adding the edge doesn't form a cycle, include it
            if dsu.union(u, v):
                mst.append((u, v, weight))
                mst_weight += weight
                
                # Optimization: Stop early when MST contains V - 1 edges
                if len(mst) == self.V - 1:
                    break

        return mst, mst_weight


# --- Driver Code Example ---
if __name__ == "__main__":
    # Create a graph with 4 vertices (0, 1, 2, 3)
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    # Run Kruskal's Algorithm
    mst_edges, total_cost = g.kruskal_mst()

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == Weight: {weight}")
    print(f"Total Weight of MST: {total_cost}")

#easy 

#A class to represent the Union-Find (Disjoint Set) data structure
class DisjointSet:
    def __init__(self, vertices):
        # Initialize each vertex as its own parent
        self.parent = {v: v for v in vertices}

    # Find the root representative of a vertex (with path compression)
    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    # Union/Merge two sets together
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root1] = root2
            return True
        return False

def kruskal(vertices, edges):
    mst = []
    
    # Step 1: Sort all edges by weight in ascending order
    # Each edge is a tuple: (weight, vertex1, vertex2)
    edges.sort()
    
    # Initialize the Disjoint Set tracking structure
    ds = DisjointSet(vertices)
    
    # Step 2: Iterate through the sorted edges
    for weight, u, v in edges:
        # Step 3: Check if the nodes are already connected
        # If union is successful, it means no cycle is formed
        if ds.union(u, v):
            mst.append((u, v, weight))
            
    return mst

# Example usage:
if __name__ == "__main__":
    # Define our graph vertices
    nodes = ['A', 'B', 'C', 'D']
    
    # Define edges: (weight, source, destination)
    graph_edges = [
        (1, 'A', 'B'),
        (3, 'A', 'C'),
        (4, 'B', 'C'),
        (2, 'B', 'D'),
        (5, 'C', 'D')
    ]
    
    minimum_spanning_tree = kruskal(nodes, graph_edges)
    
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in minimum_spanning_tree:
        print(f"{u} - {v} with weight {weight}")
