from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    heap = [(0, 0, source)]  # initialize the heap
    result = {} # store shortest path weight and edge count

    while heap: # while loop
        weight, edges, node = heappop(heap) # pop the node with smallest weight and lowest # of edges

        # checking if we've looked at this node with better or equal path
        if node in result and (weight > result[node][0] or (weight == result[node][0] and edges >= result[node][1])):
            continue

        # give this node the current shortest path
        result[node] = (weight, edges)

        # add everything updated to the heap
        for neighbor, edge_weight in graph.get(node, []):
            heappush(heap, (weight + edge_weight, edges + 1, neighbor))

    return result
    
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    queue = deque([source]) # initialize queue with source code
    parent = {source: None}  # parent of source is none cause there is no parent
    
    while queue: # while going through the queue
        node = queue.popleft() # pop the first node in the queue
        
        for neighbor in graph.get(node, []): # look at the next nodes
            if neighbor not in parent:  # checking if the node hasn't been parsed through
                parent[neighbor] = node  # set the parent as this node
                queue.append(neighbor)  # add node to the queue
    
    return parent

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = [] # building path
    node = parents[destination]  # starting at the parent

    # go backwards through tree
    while node is not None:
        path.append(node) # add node to path
        node = parents[node] # move to next node

    # flip list and return it 
    return ''.join(reversed(path))
