class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v1):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
            return True
        return False

    def print_vertex(self):
        for x, y in self.adj_list.items():
            print(f" {x}: {y}")

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, v1):
        if v1 in self.adj_list:
            for x in self.adj_list[v1]:
                self.adj_list[x].remove(v1)
            del self.adj_list[v1]
            return True
        return False


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex('C')
g.add_vertex("D")

g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("A", "C")
g.remove_edge("A", "B")
g.remove_edge("A", "D")

g.remove_vertex('D')
g.print_vertex()
