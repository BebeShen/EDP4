##### Graph #####
class Graph:
    def __init__(self) -> None:
        self.edges_list = []
    
    def add_edge(self, node1, node2, weight=1):
        self.edges_list.append([node1, node2, weight])


##### Algorithm #####
def main():
    print("Find edge disjoint path")

if __name__ == "__main__":
    main()