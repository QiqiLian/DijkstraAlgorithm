class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        distances = {v: 99 for v in self.graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            dist, curr_v = pq.pop()

            if dist > distances[curr_v]:
                continue

            for n, w in self.graph[curr_v]:
                d = dist + w
                if d < distances[n]:
                    distances[n] = d
                    pq.append((d, n))

        return distances
