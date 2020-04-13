"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # adjacency list
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # TODO
        # check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # might want to raise an exception here instead

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        que = Queue()
        que.enqueue([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while que.size() > 0:
            # dequeue/pop the first vertex
            path = que.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    que.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while stack.size() > 0:
            # dequeue/pop the first vertex
            path = stack.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create a visited set() to pass in on the recursion
        if visited is None:
            visited = set()
        # check if the node has been visited
        if starting_vertex not in visited:
            # if not...
            # mark it as visited
            print(starting_vertex)
            visited.add(starting_vertex)
            # call dft_recursive on each neighbor
            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        que = Queue()
        # enqueue A PATH TO the starting vertex
        que.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty...
        while que.size() > 0:
            # Dequeue the first PATH
            path = que.dequeue()
            # Grab the vertex from the end of the path
            # check if it's been visited
            if path[-1] not in visited:
            #if NOT
                # mark it as visited
                visited.add(path[-1])
                # check if its the target
                if path[-1] == destination_vertex:
                    # if so return the path
                    return path
                # Enqueue a Path to all its neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # make a copy of the path
                    new_path = list(path)
                    new_path.append(next_vert)
                    #enqueue copy
                    que.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while stack.size() > 0:
            # dequeue/pop the first vertex
            path = stack.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                if path[-1] == destination_vertex:
                    return path
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create a visited set() to pass in on the recursion
        if visited is None:
            visited = set()
        # check if the node has been visited
        if starting_vertex not in visited:
            # if not...
            # mark it as visited
            visited.add(starting_vertex)
            new_path = path + [starting_vertex]
            if starting_vertex == destination_vertex:
                return new_path
            # call dft_recursive on each neighbor
            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    route = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                    if route is not None:
                        return route


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
