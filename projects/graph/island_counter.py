# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

#* Notes
# islands consist of - connected components
# connected - neighbors ( edges )
# directions, nsew ( edges )
# 2D array - graph
# returns ( shape of solution ) - number of islands

# How could we write a get neighbors function that uses this shape?
# offset coordinates

# How can we find the extent of an island
# either of our traversals to find all the nodes of an island

# How do I explore the larger set
# loop through and call a traversal if we find an unvisited 1

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]