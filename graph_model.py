import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.adjList = []
        self.nodeNames = []
        self.toIndex = {}
        self.colors = []
        self.step = 0

    def load_graph(self, v, e, names, edge_list):
        self.v = v
        self.e = e
        self.nodeNames = names
        self.toIndex = {name: i for i, name in enumerate(names)}
        self.adjList = [[] for _ in range(v)]
        self.colors = [-1] * v
        self.step = 0

        for u, w in edge_list:
            ui = self.toIndex[u]
            wi = self.toIndex[w]
            self.adjList[ui].append(wi)
            self.adjList[wi].append(ui)

    def can_color(self, p, c):
        for nei in self.adjList[p]:
            if self.colors[nei] == c:
                return False
        return True

    def fill_color_layer(self, c):
        count = 0
        for i in range(self.v):
            if self.colors[i] == -1 and self.can_color(i, c):
                self.colors[i] = c
                count += 1
        return count

    def step_coloring(self):
        if all(c != -1 for c in self.colors):
            return False
        changed = self.fill_color_layer(self.step)
        self.step += 1
        return changed > 0

    def get_color_map(self):
        # Bảng màu pastel đẹp mắt
        predefined_colors = [
            "#FF6B6B", "#4ECDC4", "#FFD93D", "#1A535C", "#FF9F1C", "#6A4C93",
            "#2EC4B6", "#E71D36", "#FFB997", "#845EC2", "#00C9A7", "#F9A620",
            "#F25F5C", "#247BA0", "#70C1B3", "#B2DBBF", "#F3FFBD", "#FFE066",
        ]
        
        def rgb_from_index(index):
            if index == -1:
                return "#CCCCCC"
            return predefined_colors[index % len(predefined_colors)]

        return [rgb_from_index(c) for c in self.colors]
    
    def step_one_vertex(self):
        if all(c != -1 for c in self.colors):
            return False
        for i in range(self.v):
            if self.colors[i] == -1:
                for c in range(self.v):
                    if self.can_color(i, c):
                        self.colors[i] = c
                        return True
        return False



    def draw_graph(self):
        G = nx.Graph()
        for name in self.nodeNames:
            G.add_node(name)

        for i, neighbors in enumerate(self.adjList):
            for j in neighbors:
                if i < j:
                    G.add_edge(self.nodeNames[i], self.nodeNames[j])

        pos = nx.spring_layout(G, seed=42)
        colors = self.get_color_map()
        nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1000, font_weight='bold', font_color='white')
        return plt.gcf()
