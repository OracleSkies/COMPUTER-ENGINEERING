from icecream import ic
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # For undirected graph

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adj in self.graph[vertex]:
                self.graph[adj].remove(vertex)
            del self.graph[vertex]

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        bfs_order = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                bfs_order.append(vertex)
                visited.add(vertex)
                queue.extend([v for v in self.graph[vertex] if v not in visited])
        
        return bfs_order

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        dfs_order = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                dfs_order.append(vertex)
                visited.add(vertex)
                stack.extend([v for v in self.graph[vertex] if v not in visited])
        
        return dfs_order

    def find_path(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in self.graph:
            return None
        for vertex in self.graph[start_vertex]:
            if vertex not in path:
                new_path = self.find_path(vertex, end_vertex, path)
                if new_path:
                    return new_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for vertex in self.graph[start_vertex]:
            if vertex not in path:
                new_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def is_connected(self):
        start_vertex = list(self.graph.keys())[0]
        visited = self.dfs(start_vertex)
        return len(visited) == len(self.graph)

    def has_cycle(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                if self._has_cycle(vertex, visited, -1):
                    return True
        return False

    def _has_cycle(self, vertex, visited, parent):
        visited.add(vertex)
        for adj in self.graph[vertex]:
            if adj not in visited:
                if self._has_cycle(adj, visited, vertex):
                    return True
            elif parent != adj:
                return True
        return False
    
graph = Graph()



#strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#listahan = []

jomer = "JOMERJOHNLEJANO"
joph = "JOPHANTHONYGARAGARAMANOSCA"
inay = "CHRISTIANBANTACULOINAY"

nameList = []
nameList.extend(jomer)
nameList.extend(joph)
nameList.extend(inay)
counts = {}

def addVertexLoop(names,counter):
    for letter in names:
        count = counter.get(letter,0)
        if count == 0:
            graph.add_vertex(letter)
        else:
            graph.add_vertex(letter + str(count))
        counter[letter] = count + 1

def addBFSEdge(vertices: dict) -> None:
    root = vertices[0]
    stack = [root]
    i = 1

    while stack and i < len(vertices):
        current = stack.pop(0)
        children = 2
        for _ in range(children):
            if i < len(vertices):
                child = vertices[i]
                graph.add_edge(current, child)
                stack.append(child)
                i += 1


addVertexLoop(nameList,counts)
vertices = list(graph.graph.keys())
addBFSEdge(vertices)

#print(graph.graph)
#print(graph.bfs(vertices[0]))
#print(graph.dfs("A"))

def pyramidPrint(rows):

  # Upper half of the diamond
  for i in range(rows):
    spaces = " " * (rows - i - 1)
    stars =  vertices[i] * (2 * i + 1)
    print(spaces + stars)

pyramidPrint(7)