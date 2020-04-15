from string import ascii_lowercase
# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None
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
a_file = open("words.txt", "r")
list_of_lists = []
list_of_words = set()
for line in a_file:
    stripped_line = line.strip()
    list_of_words.add(stripped_line)
    line_list = stripped_line.split()
    list_of_lists.append(line_list)
a_file.close()


def string_transform(begin_word, end_word):
    if len(begin_word) is not len(end_word):
        return None
    graph = Graph()
    split_word = begin_word.split("")
    graph.add_vertex(begin_word)
    for i, letter in enumerate(split_word):
        for c in ascii_lowercase:
            new_word = split_word.copy()
            new_word[i] = c
            joined = "".join(new_word)
            if joined in list_of_words:
                graph.add_vertex(joined)
                graph.add_edge(begin_word, joined)
    # for i in range(0, len(split_word)):
    #     for c in ascii_lowercase:
    #         # loop through words
    #         # if word is valid
    #         # add as vertex
    #         # create edge between words