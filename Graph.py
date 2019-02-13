# Python program for
# validation of a graph

# import dictionary for graph
from collections import defaultdict
# function for adding edge to graph
graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)
# definition of function
def generate_edges(graph):
    edges = [] #list that will keep the edges list
    # for each node in graph
    for node in graph:
        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    return edges

# function to find path
def find_path(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return path
  for node in graph[start]:
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath:
        return newpath
      return None

# function to generate all possible paths
def find_all_paths(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return [path]
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
    for newpath in newpaths:
      paths.append(newpath)
  return paths

# function to find the shortest path
def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

# declaration of graph as dictionary
addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'c')
addEdge(graph, 'b', 'e')
addEdge(graph, 'c', 'd')
addEdge(graph, 'c', 'e')
addEdge(graph, 'c', 'a')
addEdge(graph, 'c', 'b')
addEdge(graph, 'e', 'b')
addEdge(graph, 'd', 'c')
addEdge(graph, 'e', 'c')

# Driver Function call
# to print generated graph
print(generate_edges(graph))
# Driver function call to print the path
print(find_path(graph, 'd', 'c'))
# Driver function call to print all generated paths
print(find_all_paths(graph, 'd', 'c'))
# Driver function call to print
# the shortest path
print(find_shortest_path(graph, 'a', 'e'))