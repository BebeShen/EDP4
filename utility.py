##### Graph #####
class Graph:
    def __init__(self, num_of_nodes, direction=True) -> None:
        self.edges_list = []
        self.num_of_nodes = num_of_nodes
        self.direction = direction

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns
        self.adj_matrix = [[0 for column in range(num_of_nodes)] 
                            for row in range(num_of_nodes)]
    
    def add_edge(self, node1, node2, weight=1):
        self.edges_list.append([node1, node2, weight])
        self.adj_matrix[node1][node2] = weight
        
        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.direction:
            self.edges_list.append([node2, node1, weight])
            self.adj_matrix[node2][node1] = weight
    
    def print_edge_list(self):
        num_of_edges = len(self.edges_list)
        print("------------------------")
        print("List:")
        for i in range(num_of_edges):
            print("edge ", i+1, ": ", self.edges_list[i])
        print()
        print("ADJ matrix:")
        for i in range(self.num_of_nodes):
            print(self.adj_matrix[i])
        print("------------------------")
        