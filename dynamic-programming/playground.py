class Graph:
    def __init__(self):
        self.vertices = {
            "S":["A"],
            "A": ["B", "C"],
            "B": ["C", "D"],
            "C": ["D", "E", "F"],
            "D": ["F"],
            "E": ["F"],
            "F": []
        }

        self.weights = {
            
        }