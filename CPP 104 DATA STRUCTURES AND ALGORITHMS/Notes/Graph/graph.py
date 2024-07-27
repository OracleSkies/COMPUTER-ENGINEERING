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

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): #insert at end
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node    
### Output
graph = Graph()
link = LinkedList()


#print(graph.dfs("J"))

jomer = "JOMERJOHNLEJANODONASCO"
joph = "JOPHANTHONYGARAGARAMANOSCA"
inay = "CHRISTIANBANTACULOINAY"
nameList = []
nameList.extend(jomer)
nameList.extend(joph)
nameList.extend(inay)


testList = []
testList.extend(jomer)
endList = []


for letter in nameList:
    if letter not in endList:
        endList.append(letter)
        graph.add_vertex(letter)
    else:
        newLetter = letter + str(endList.count(letter))
        if newLetter not in endList:
            endList.append(newLetter)
            graph.add_vertex(newLetter)
        else:
            endList.append(newLetter+str(endList.count(letter)+1))
            graph.add_vertex(newLetter+str(endList.count(letter)+1))

print(graph.graph)

'''
#print(nameList)
counter = 0
for letter in testList:
    if letter not in endList:
        endList.append(letter)
        #graph.add_vertex(letter)
    else:
        for letter in endList:
            counter += 1
            endList.append(letter + str(counter))
        #print(counter)
        counter = 0

#print(endList)


        
    
#print(graph.graph)'''



