import math
import heapq
from route_planner.helpers import load_map

def cal_distance(M, node_1, node_2):
    coord_1 = M.intersections[node_1]
    coord_2 = M.intersections[node_2]
    return math.sqrt((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_2[1]) ** 2)


def shortest_path(M, start, goal):
    print("shortest path called")
    distance_library = {node: (math.inf, math.inf, []) for node in M.intersections}  # {node : (indicator, distance, path=[])
    indicator_start_node = 0 + cal_distance(M, start, goal)
    distance_library[start] = indicator_start_node, 0, [start]

    frontiers = [(indicator_start_node, (start, [start], 0))]  # frontiers: (indicator, (node, path=[], distance))

    while len(frontiers) > 0:
        current_min_indicator, (current_min_node, current_min_path, current_min_distance) = heapq.heappop(frontiers)
        if current_min_distance < distance_library[current_min_node][1]:
            distance_library[current_min_node] = current_min_indicator, current_min_distance, current_min_path

        # Check all the neighbors, mark them as frontier and select the one with the least g + h as visited.
        for neighbor in M.roads[current_min_node]:

            straight_dis_to_goal = cal_distance(M, neighbor, goal)
            cost = cal_distance(M, current_min_node, neighbor)

            new_distance = cost + current_min_distance
            indicator = straight_dis_to_goal + cost
            if new_distance < distance_library[neighbor][1]:
                new_path = current_min_path + [neighbor]

                distance_library[neighbor] = (indicator, new_distance, new_path)
                heapq.heappush(frontiers, (indicator, (neighbor, new_path, new_distance)))

    return distance_library[goal][2]


map_40 = load_map('map-40.pickle')
path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)