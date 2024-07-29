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

### Output
graph = Graph()

jomer = "JOMERJOHNLEJANODONASCO"
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

def addBFSEdge():
    graph.graph.clear()
    addVertexLoop(nameList,counts)
    vertexList = list(graph.graph.keys())
    root = vertexList[0]
    stack = [root]
    count = 1

    while stack and count < len(vertexList):
        current = stack.pop(0)
        children = 2
        for _ in range(children):
            if count < len(vertexList):
                child = vertexList[count]
                graph.add_edge(current, child)
                stack.append(child)
                count += 1
    
    output = numberRemove(graph.bfs(vertexList[0]))
    return output

def addDFSEdge():
    graph.graph.clear()
    counts.clear()
    addVertexLoop(nameList,counts)
    vertexList = list(graph.graph.keys())
    #JOMER
    graph.add_edge("J","R2")
    graph.add_edge("J","O")
    graph.add_edge("O","P")
    graph.add_edge("O","M")
    graph.add_edge("M","N2")
    graph.add_edge("M","E")
    graph.add_edge("E","J2")
    graph.add_edge("E","R")
    graph.add_edge("R","N")
    graph.add_edge("R","J1")
    graph.add_edge("J1","H")
    graph.add_edge("J1","O1")
    graph.add_edge("N","E1")
    graph.add_edge("N","L")
    graph.add_edge("J2","D")
    graph.add_edge("J2","A")
    graph.add_edge("A","O2")
    graph.add_edge("A","N1")
    graph.add_edge("D","O3")
    graph.add_edge("N2","O4")
    graph.add_edge("N2","A1")
    graph.add_edge("A1","C")
    graph.add_edge("A1","S")

    #JOPH
    graph.add_edge("O4","O5")
    graph.add_edge("O4","J3")
    graph.add_edge("P","Y")
    graph.add_edge("P","H1")
    graph.add_edge("H1","H2")
    graph.add_edge("H1","A2")
    graph.add_edge("A2","T")
    graph.add_edge("A2","N3")
    graph.add_edge("H2","N4")
    graph.add_edge("H2","O6")
    graph.add_edge("Y","A4")
    graph.add_edge("Y","G")
    graph.add_edge("G","R1")
    graph.add_edge("G","A3")
    graph.add_edge("A4","A5")
    graph.add_edge("A4","G1")
    graph.add_edge("R2","A9")
    graph.add_edge("R2","A6")
    graph.add_edge("A6","C2")
    graph.add_edge("A6","M1")
    graph.add_edge("M1","S1")
    graph.add_edge("M1","A7")
    graph.add_edge("A7","O7")
    graph.add_edge("A7","N5")
    graph.add_edge("S1","A8")
    graph.add_edge("S1","C1")

    #INAY
    graph.add_edge("C2","S2")
    graph.add_edge("C2","H3")
    graph.add_edge("H3","I")
    graph.add_edge("H3","R3")
    graph.add_edge("S2","I1")
    graph.add_edge("S2","T1")
    graph.add_edge("A9","U")
    graph.add_edge("A9","N6")
    graph.add_edge("N6","T2")
    graph.add_edge("N6","B")
    graph.add_edge("B","N7")
    graph.add_edge("B","A10")
    graph.add_edge("T2","C3")
    graph.add_edge("T2","A11")
    graph.add_edge("U","N8")
    graph.add_edge("U","L1")
    graph.add_edge("L1","I2")
    graph.add_edge("L1","O8")
    graph.add_edge("N8","Y1")
    graph.add_edge("N8","A12")
    output = numberRemove(graph.dfs(vertexList[0]))
    return output

def numberRemove(array):
    output = []
    for element in array:
        output.append(element[0])
    return output

print("===BREADTH FIRST SEARCH===")
print(addBFSEdge())
print()
print("===DEPTH FIRST SEARCH===")
print(addDFSEdge())
