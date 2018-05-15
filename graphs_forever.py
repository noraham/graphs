"""Graph stuff!"""

from unittest import TestCase 

##########
""" Graph ADT:
    Graph() creates a new empty Graph
    addVertex(vert) adds instance of vertex to Graph
    addEdge(fromVert, toVert[, weight]) new directed edge in graph
    getVertex(vert) finds vertex in graph
    getVertices() returns all vertices in graph
    vertex in Graph sould return True or False  """
##########

class Node(object):
    """simple node to use in Queue"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    """Best way to search a graph is BFS, which is with a queue.
       This is a simple queue class to use when searching a graph."""

    def __init__(self):
        """Initialize and empty queue, with head and tail attributes"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """add to end of queue"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        """remove from start of queue"""
        popped = self.head
        self.head = self.head.next
        return popped

    def is_empty(self):
        """returns True if queue is empty, False if there are items in the queue"""
        if self.head == None:
            return True
        return False

class Vertex(object):
    """vertex is a node in the graph.
       For weighted adjacencies, use a dictionary, for unweighted a set is fine.
       A vertex holds data and adjacency info.
       Initaite a vertex with just its data, then assign neighbors."""

    def __init__(self, data):
        self.data = data
        self.adj = set()

    def add_adj(self, adj_vert):
        """for unweighted adjacencies, adds adjacent vertex to this vertex's
           adj set"""
        self.adj.add(adj_vert)

    def get_adj(self):
        """returns adj set for given vertex"""
        return self.adj


class Graph(object):
    """See ADT above for summary of functions.
       A graph contains 'components', collections of adjacent vertices.
       A dictionary that maps vertex names to data."""

    def __init__ (self):
        """create new, empty graph (dictionary)"""
        self.vertices = {}
        self.total = 0

    def add_vertex(self, data):
        """instantiates Vertex ojject, adds to graph"""
        self.total += 1
        instantiated = Vertex(data)
        self.vertices[data] = instantiated
        return instantiated

    def add_edge(self, from_vert, to_vert):
        """new directed edge between these 2 vertices"""
        self.vertices[from_vert].add_adj(self.vertices[to_vert])

    def get_vertex(self, data):
        """returns vertex obj matching data"""
        if data in self.vertices:
            return self.vertices[data]
        return None

    def get_vertices(self):
        """return list of all vertices in graph"""
        return self.vertices.keys()

    def __contains__(self, data):
        """what is this magic???"""
        return data in self.vertices

    def are_connected_BFS(self, start_vertex, sought):
        """given starting vertex, return True if sought data is connected to start.
           Returns False if sought is not connected
           To turn this into counting degrees of distance, have to change vertex
           class to include a distance attribute on the object that you can both
           set and get; set distance when adj are enqueued, +1 from current's
           distance, then return distance of sought when it is reached."""

        gray = Queue()
        gray.enqueue(start_vertex)
        black = set()
        black.add(start_vertex.data)

        while not gray.is_empty():
            current = gray.dequeue()
            if current.data.data == sought:
                return True
            else:
                for white in current.data.adj - black:
                    gray.enqueue(white)
                    black.add(white)        
        return False

    def are_connected_DFS(self, start_vertex, sought):
        """Recursive, uses call stack for dfs"""

        # set up this variable in first call, don't do this in other calls
        seen = set()

        def _are_connected_DFS(vertex, sought):
            """recursive function"""
            if vertex.data == sought:
                return True
            seen.add(vertex)
            for each in vertex.adj - seen:
                if _are_connected_DFS(each, sought):
                    return True
            return False

        return _are_connected_DFS(start_vertex, sought)

    def topo_sort(self, start_vertex):
        """Implements DFS non-recursively, counts finish time for each vertex.
           Uses finish time to return topo sort"""

        # give graph new attribute, time
        self.time = 0
        all_vertices = self.get_vertices()
        unseen = set(all_vertices)

        #iterate over each vertex in graph
        for each_vertex in all_vertices:
            if each_vertex in unseen:
                self.dfsvisit(each_vertex, unseen)

    def dfsvisit(self, start_vertex, unseen):
        self.time += 1 # use this to set disocvery time
        start_vertex.discovery = self.time
        for next_vertex in start_vertex.get_vertices():
            if next_vertex in unseen:
                self.dfsvisit(next_vertex)
        unseen.remove(start_vertex)
        self.time += 1 # use this to set finish time
        start_vertex.finish = self.time # like a time stamp for when all dependencies finish

        # get all vertices and finish times, sort high to low finish time, return




class UnitTests(TestCase):
    """Tests the classes and functions in this file"""

    def test_graph(self):
        """tests Graph instantiation, Vertex instantiation, and get_vert method,
        are_connected methods."""

        g = Graph()
        g.add_vertex('a')
        g.add_vertex('b')
        g.add_vertex('c')
        g.add_vertex('d')
        g.add_vertex('e')
        test = g.get_vertices()
        test.sort()
        control = ['a', 'b', 'c', 'd', 'e']
        assert test == control

        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'd')
        g.add_edge('d', 'e')
        test = g.get_vertex('a').get_adj()
        for item in test:
            assert item.data == 'b'
        test = g.get_vertex('d').get_adj()
        for item in test:
            assert item.data == 'e'

        a_vertex = g.get_vertex('a')
        assert g.are_connected_BFS(a_vertex, 'd') is True
        assert g.are_connected_BFS(a_vertex, 'f') is False
        e_vertex = g.get_vertex('e')
        assert g.are_connected_BFS(e_vertex, 'a') is False

        a_vertex = g.get_vertex('a')
        assert g.are_connected_DFS(a_vertex, 'd') is True
        assert g.are_connected_DFS(a_vertex, 'f') is False
        e_vertex = g.get_vertex('e')
        assert g.are_connected_DFS(e_vertex, 'a') is False


if __name__ == "__main__":
    import unittest
    unittest.main()
