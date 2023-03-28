import heapq
import math

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# A* algorithm implementation
def a_star(start, goal, obstacles):
    # Set of visited nodes
    visited = set()

    # Priority queue for open nodes
    queue = [(0, start)]
    heapq.heapify(queue)

    # Map of nodes to their parents
    parent_map = {}

    # Map of nodes to their g_scores (costs of getting to that node)
    g_score = {start: 0}

    # Map of nodes to their f_scores (estimated total costs to reach goal through that node)
    f_score = {start: euclidean_distance(start, goal)}

    # Main loop
    while queue:
        # Get the node with the lowest f_score from the queue
        current = heapq.heappop(queue)[1]

        # If we have reached the goal, reconstruct and return the path
        if current == goal:
            path = []
            while current in parent_map:
                path.append(current)
                current = parent_map[current]
            path.reverse()
            return path

        # Add the current node to the set of visited nodes
        visited.add(current)

        # Generate the neighbors of the current node
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor = (current[0] + i, current[1] + j)

                # Skip the current node and obstacles
                if (i, j) == (0, 0) or neighbor in obstacles:
                    continue

                # Calculate the tentative g_score for the neighbor
                tentative_g_score = g_score[current] + euclidean_distance(current, neighbor)

                # If the neighbor has already been visited and the tentative g_score is greater than the recorded g_score,
                # skip this neighbor
                if neighbor in visited and tentative_g_score >= g_score.get(neighbor, float('inf')):
                    continue

                # Update the parent, g_score, and f_score of the neighbor
                parent_map[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + euclidean_distance(neighbor, goal)

                # Add the neighbor to the priority queue
                heapq.heappush(queue, (f_score[neighbor], neighbor))

    # If we have exhausted all possible paths without reaching the goal, return None
    return None
