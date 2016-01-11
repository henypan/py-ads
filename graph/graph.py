class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbors(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connectedTo[neighbor]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += self.num_vertices + 1
        new_vertext = Vertex(key)
        self.vert_list[key] = new_vertext
        return new_vertext

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            node = self.add_vertex(f)
        if t not in self.vert_list:
            node = self.add_vertex(t)
        self.vert_list[f].add_neighbors(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

g = Graph()
for i in range(6):
    g.add_vertex(i)
print g.vert_list
g.add_edge(0, 1, 5)
g.add_edge(0, 5, 2)
g.add_edge(1, 2, 1)
g.add_edge(1, 4, 2)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 3)
g.add_edge(4, 0, 1)
g.add_edge(5, 4, 10)
g.add_edge(5, 2, 1)

for v in g:
    for w in v.get_connections():
        print "(%s, %s, %s)" % (v.get_id(), w.get_id(), str(v.get_weight(w)))
