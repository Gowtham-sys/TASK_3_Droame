def cost(state):
    import numpy as np

    total_cost = 0
    
    # calculate distance cost
    for i, drone in enumerate(state):
        distance = np.linalg.norm(drone["position"] - drone["destination"])
        total_cost += distance
        
    # calculate collision cost
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if np.array_equal(state[i]["position"], state[j]["position"]):
                total_cost += 100000  # large penalty for collision
                
    return total_cost
