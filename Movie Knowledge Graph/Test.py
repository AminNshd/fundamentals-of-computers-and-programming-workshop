class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False
        
    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False
        
    def __repr__(self):
        return str(self.neighbors)


class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors

            
    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors
            
    def add_edge(self, vertex_from, vertex_to):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            vertex_from.add_neighbor(vertex_to)
            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors
                
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0],edge[1])          
    
    def adjacencyMatrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(g.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names)))) 
            import numpy as np
            self.adjacency_matrix = np.zeros(shape=(len(self.vertices),len(self.vertices)))
            for i in range(len(self.vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in g.vertices[self.vertex_names[i]]:
                        j = g.vertex_indices[el]
                        self.adjacency_matrix[i,j] = 1
            return self.adjacency_matrix
        else:
            return dict()              
                        
def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyMatrix())


movieData = [
    {
        "name": "Heat",
        "type": "movie",
        "year": 1995,
        "genre": "Crime, Drama, Action",
        "actors": ["Al Pacino", "Robert De Niro", "Val Kilmer"],
        "directors": ["Michael Mann"]
    },
    {
        "name": "Silver Linings Playbook",
        "type": "movie",
        "year": 2012,
        "genre": "Comedy, Drama, Romance",
        "actors": ["Bradley Cooper", "Jennifer Lawrence", "Robert De Niro"],
        "directors": ["David O. Russell"]
    },
    {
        "name": "The Departed",
        "type": "movie",
        "year": 2006,
        "genre": "Crime, Drama, Thriller",
        "actors": ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson", "Mark Wahlberg"],
        "directors": ["Martin Scorsese"]
    },
    {
        "name": "Ocean's Eleven",
        "type": "movie",
        "year": 2001,
        "genre": "Crime, Drama, Thriller",
        "actors": ["George Clooney", "Brad Pitt", "Matt Damon", "Julia Roberts"],
        "directors": ["Steven Soderbergh"]
    },
    {
        "name": "The Avengers",
        "type": "movie",
        "year": 2012,
        "genre": "Action, Adventure, Sci-Fi",
        "actors": ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo"],
        "directors": ["Joss Whedon"]
    },
    {
        "name": "No Country for Old Men",
        "type": "movie",
        "year": 2007,
        "genre": "Crime, Drama, Thriller",
        "actors": ["Josh Brolin", "Javier Bardem", "Tommy Lee Jones"],
        "directors": ["Joel Coen", "Ethan Coen"]
    },
    {
        "name": "The Social Network",
        "type": "movie",
        "year": 2010,
        "genre": "Biography, Drama",
        "actors": ["Jesse Eisenberg", "Andrew Garfield", "Justin Timberlake"],
        "directors": ["David Fincher"]
    },
    {
        "name": "The Great Gatsby",
        "type": "movie",
        "year": 2013,
        "genre": "Drama, Romance",
        "actors": ["Leonardo DiCaprio", "Tobey Maguire", "Carey Mulligan"],
        "directors": ["Baz Luhrmann"]
    },
    {
        "name": "American Hustle",
        "type": "movie",
        "year": 2013,
        "genre": "Crime, Drama",
        "actors": ["Christian Bale", "Bradley Cooper", "Amy Adams", "Jennifer Lawrence"],
        "directors": ["David O. Russell"]
    },
    {
        "name": "The Wolf of Wall Street",
        "type": "movie",
        "year": 2013,
        "genre": "Biography, Comedy, Crime",
        "actors": ["Leonardo DiCaprio", "Jonah Hill", "Margot Robbie"],
        "directors": ["Martin Scorsese"]
    }
]

target = input("Enter your target: ")
type = input("Enter your targets type: ")
search = input("Enter the type you are searching about your target: ")

t = Vertex(target)
resultList = []
for i in range(len(movieData)):
    for j in range(len(movieData[i])):
