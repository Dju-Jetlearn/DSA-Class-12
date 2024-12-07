class Graph():
    def __init__(self, n):
        self.n = n
        self.adj = [[]*n for i in range(n)]

    def edgecreate(self, a, b):
        self.adj[a-1].append(b-1)
        self.adj[b-1].append(a-1)
    
    def BFS(self, source):
        visited = [False]*self.n
        queue = []
        queue.append(source)
        visited[source] = True
        res = []
        while len(queue) > 0:
            s = queue.pop(0)
            res.append(s)
            for node in self.adj[s]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
        return res
    
graph = Graph(4)
graph.edgecreate(1,2)
graph.edgecreate(1,3)
graph.edgecreate(2,4)
graph.edgecreate(3,4)

print(graph.BFS(2))