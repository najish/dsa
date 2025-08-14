from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}
    

    def add_vertex(self,vertex):
        graph = self.graph 
        
        if vertex in graph:
            print('vertex is already added')
        else:
            graph[vertex] = set()

    
    def add_edge(self,source,dest):
        graph = self.graph
        if source != dest:
            if source in graph and dest in graph:
                graph[source].add(dest)
                graph[dest].add(source)
            else:
                print('give valid vertices')

    def __str__(self):
        return "\n".join(f"{v} -> {sorted(neigh)}" for v, neigh in self.graph.items())
        


    def dfs(self,vertex, visited = None):
        graph = self.graph 
        if visited is None:
            visited = set()
        if vertex in visited:
            return 
        
        visited.add(vertex)
        print(f"{vertex} ->", end=' ')
        for item in graph[vertex]:
            self.dfs(item, visited)

    def bfs(self, vertex, visited=None):

        if visited is None:
            visited = set()
        
        graph = self.graph
        queue = deque([vertex])

        while len(queue) != 0:
            vertex = queue.popleft()

            if vertex not in visited:
                print(f"{vertex}->", end=' ')
                visited.add(vertex)

            for item in graph[vertex]:
                if item not in visited:
                    queue.append(item)



graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Adding edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')
graph.add_edge('B', 'E')


graph.dfs('A')
print()
graph.bfs('B')