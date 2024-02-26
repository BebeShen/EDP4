from utility import *


##### Algorithm #####
def main():
    print("Find edge disjoint path")
    graph = Graph(5,False)

    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 15)
    graph.add_edge(4, 2, 7)
    graph.add_edge(4, 3, 11)

    graph.print_edge_list()

if __name__ == "__main__":
    main()