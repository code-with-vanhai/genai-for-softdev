import heapq
import re
from collections import defaultdict


class InvalidLocationError(Exception):
    """Custom exception for invalid location names."""
    pass


class GraphCapacityError(Exception):
    """Custom exception for exceeding graph capacity."""
    pass


class SecureGraph:
    def __init__(self, max_nodes=1000):
        self.graph = defaultdict(dict)
        self.max_nodes = max_nodes  # Limit the number of nodes to prevent DoS

    def _is_valid_location(self, location):
        """Check if the location is a valid string."""
        return isinstance(location, str) and re.match(r"^[\w\s-]+$", location)

    def add_location(self, location):
        """Add a new location (node) to the graph securely."""
        if not self._is_valid_location(location):
            raise InvalidLocationError("Invalid location name. Only letters, numbers, spaces, and hyphens allowed.")

        if location not in self.graph:
            if len(self.graph) < self.max_nodes:
                self.graph[location] = {}
            else:
                raise GraphCapacityError("Node limit reached. Cannot add more locations.")
        else:
            print(f"Location '{location}' already exists.")

    def add_road(self, location1, location2, distance):
        """Add a road (edge) securely between two locations."""
        if not all(map(self._is_valid_location, [location1, location2])):
            raise InvalidLocationError("Invalid location names.")

        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Distance must be a positive number.")

        # Ensure locations exist before adding a road
        self.add_location(location1)
        self.add_location(location2)

        # Ensure roads are stored uniquely using sorted tuples
        key = tuple(sorted([location1, location2]))
        if key in self.graph[location1]:
            print(f"Road already exists between {location1} and {location2}")
            return

        self.graph[location1][location2] = distance
        self.graph[location2][location1] = distance  # Undirected graph

    def get_locations(self):
        """Return all locations (nodes) securely."""
        return list(self.graph.keys())

    def get_roads(self):
        """Return all roads (edges) securely."""
        roads = set()
        for location in self.graph:
            for neighbor, distance in self.graph[location].items():
                key = tuple(sorted([location, neighbor]))
                if key not in roads:
                    roads.add((location, neighbor, distance))
        return list(roads)

    def find_shortest_path(self, start, end):
        """Find the shortest path securely using Dijkstra's algorithm."""
        if start not in self.graph or end not in self.graph:
            raise ValueError("One or both locations do not exist in the graph.")

        priority_queue = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous_nodes = {}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                path = []
                while current_node:
                    path.insert(0, current_node)
                    current_node = previous_nodes.get(current_node)
                return path, distances[end]

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return None, float('inf')


# Example usage with 10 nodes
if __name__ == "__main__":
    try:
        hanoi_secure_graph = SecureGraph(max_nodes=10)
        
        # Adding 10 nodes with connecting roads
        hanoi_secure_graph.add_road("Hoan Kiem", "Ba Dinh", 2)
        hanoi_secure_graph.add_road("Ba Dinh", "Tay Ho", 4)
        hanoi_secure_graph.add_road("Tay Ho", "Cau Giay", 3)
        hanoi_secure_graph.add_road("Hoan Kiem", "Dong Da", 5)
        hanoi_secure_graph.add_road("Dong Da", "Cau Giay", 1)
        hanoi_secure_graph.add_road("Ba Dinh", "Dong Da", 2)
        hanoi_secure_graph.add_road("Cau Giay", "Thanh Xuan", 6)
        hanoi_secure_graph.add_road("Thanh Xuan", "Ha Dong", 3)
        hanoi_secure_graph.add_road("Ha Dong", "Long Bien", 7)
        hanoi_secure_graph.add_road("Long Bien", "Tay Ho", 8)

        print("Locations:", hanoi_secure_graph.get_locations())
        print("Roads:", hanoi_secure_graph.get_roads())

        # Finding shortest path from "Hoan Kiem" to "Ha Dong"
        shortest_path, distance = hanoi_secure_graph.find_shortest_path("Hoan Kiem", "Ha Dong")
        print(f"Shortest path: {shortest_path}, Distance: {distance}")

    except (InvalidLocationError, GraphCapacityError, ValueError) as e:
        print("Error:", e)
