import heapq
import random
import re
import time
from collections import defaultdict


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
            raise ValueError("Invalid location name. Only letters, numbers, spaces, and hyphens allowed.")

        if location not in self.graph:
            if len(self.graph) < self.max_nodes:
                self.graph[location] = {}
            else:
                raise MemoryError("Node limit reached. Cannot add more locations.")

    def add_road(self, location1, location2, distance):
        """Add a road (edge) securely between two locations."""
        if not all(map(self._is_valid_location, [location1, location2])):
            raise ValueError("Invalid location names.")

        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Distance must be a positive number.")

        # Ensure locations exist before adding a road
        self.add_location(location1)
        self.add_location(location2)

        self.graph[location1][location2] = distance
        self.graph[location2][location1] = distance  # Undirected graph

    def get_locations(self):
        """Return all locations (nodes) securely."""
        return list(self.graph.keys())

    def find_nearest_neighbor_tsp(self, start):
        """Solve the Travelling Salesperson Problem using Nearest Neighbor heuristic."""
        start_time = time.time()  # Start timing

        unvisited = set(self.graph.keys())
        path = []
        current = start
        total_distance = 0

        while unvisited:
            path.append(current)
            unvisited.remove(current)

            nearest_neighbor = None
            shortest_distance = float('inf')

            for neighbor, distance in self.graph[current].items():
                if neighbor in unvisited and distance < shortest_distance:
                    nearest_neighbor = neighbor
                    shortest_distance = distance

            if nearest_neighbor is None:
                break  # All nodes visited

            total_distance += shortest_distance
            current = nearest_neighbor

        # Return to start node to complete the cycle
        if path[0] in self.graph[path[-1]]:
            total_distance += self.graph[path[-1]][path[0]]
            path.append(path[0])

        end_time = time.time()  # End timing
        execution_time = end_time - start_time

        return path, total_distance, execution_time


# Generate 1000 nodes with random distances
def generate_large_graph(graph, num_nodes):
    locations = [f"Node_{i}" for i in range(1, num_nodes + 1)]

    for location in locations:
        graph.add_location(location)

    # Randomly connect nodes with distances between 1 and 100
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            distance = random.randint(1, 100)
            graph.add_road(locations[i], locations[j], distance)


# Example usage with 1000 nodes
if __name__ == "__main__":
    large_graph = SecureGraph(max_nodes=1000)

    print("Generating 1000-node graph...")
    generate_large_graph(large_graph, 1000)
    print("Graph generation completed.")

    # Find a route using Nearest Neighbor from Node_1
    start_node = "Node_1"
    path, total_distance, execution_time = large_graph.find_nearest_neighbor_tsp(start_node)

    print(f"Route visiting all nodes starting from {start_node}:")
    print(" -> ".join(path[:20]) + " ...")  # Print first 20 nodes to avoid clutter
    print(f"Total travel distance: {total_distance}")
    print(f"Time taken to visit all nodes: {execution_time:.4f} seconds")
