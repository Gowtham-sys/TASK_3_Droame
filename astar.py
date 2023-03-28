import heapq
import numpy as np

# Define the grid size and drone size
GRID_SIZE = (20, 20)
DRONE_SIZE = (1, 1)

# Define the adjacency of cells
ADJACENCY = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

# Define the A* pathfinding algorithm
def a_star(start_state, goal_states, h_func):
    # Define the cost function
    def cost_func(state, action):
        cost = np.inf
        new_state = np.array(state)
        for i, drone_goal in enumerate(goal_states):
            drone_pos = state[i*4:(i+1)*4][:2]
            dist = np.linalg.norm(drone_pos - drone_goal)
            if dist == 0:
                continue
            new_drone_pos = drone_pos + action[i*2:(i+1)*2]
            if any(new_drone_pos < 0) or any(new_drone_pos + DRONE_SIZE > GRID_SIZE):
                return np.inf
            for j in range(i+1, len(goal_states)):
                other_drone_pos = new_state[j*4:(j+1)*4][:2]
                if np.array_equal(new_drone_pos, other_drone_pos):
                    return np.inf
            cost = min(cost, dist)
        return cost

    # Define the state class
    class State:
        def __init__(self, state, action=None, g=0, h=0, parent=None):
            self.state = state
            self.action = action
            self.g = g
            self.h = h
            self.parent = parent

        def __lt__(self, other):
            return self.g + self.h < other.g + other.h

    # Initialize the open and closed lists
    start_node = State(start_state, g=0, h=h_func(start_state, goal_states))
    open_list = [start_node]
    closed_list = set()

    # Loop until the goal state is reached or the open list is empty
    while open_list:
        # Pop the node with the lowest f value
        curr_node = heapq.heappop(open_list)

        # Check if the goal state has been reached
        if all(np.all(np.isclose(curr_node.state[i*4:(i+1)*4][:2], goal_states[i])) for i in range(len(goal_states))):
            path = []
            while curr_node.parent is not None:
                path.append(curr_node.action)
                curr_node = curr_node.parent
            return list(reversed(path))

        # Generate the successor states and add them to the open list
        for action in ADJACENCY:
            new_state = np.array(curr_node.state) + np.array([action[0], action[1], 0, 0]*len(goal_states))
            cost = cost_func(curr_node.state, np.array([action[0], action[1]]*len(goal_states)))
            new_node = State(new_state, action, g=curr_node.g + cost, h=h_func(new_state, goal_states), parent=curr_node)
            if tuple(new_state) not in closed_list:
                heapq.heappush(open_list, new_node)
                closed_list.add(tuple(new_state))

    # If the open list is empty, then there is no path to the goal state
    return None
