def can_color(coloring, region, color, adjacency_list):
    for neighbor in adjacency_list[region]:
        if coloring.get(neighbor) == color:
            return False
    return True

def color_map(adjacency_list, colors, region, coloring, all_solutions, solutions):
    if region == len(adjacency_list):
        print(coloring) if not all_solutions else solutions.append(dict(coloring))
        return True if not all_solutions else False

    for color in colors:
        if can_color(coloring, region, color, adjacency_list):
            coloring[region] = color
            if not color_map(adjacency_list, colors, region + 1, coloring, all_solutions, solutions):
                if not all_solutions:
                    return True
            del coloring[region]
    
    return False if not all_solutions else solutions

# Like Austrila
regions = 7
adjacency_list = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3, 4, 5], 3: [1, 2, 4], 4: [2, 3, 5], 5: [2, 4, 6], 6: [5]}  
colors = ['red', 'green', 'blue'] 

solutions = []
# Map nodes and conncections, colors, starting node, current coloring, do I want all soliuions, solutions dict
color_map(adjacency_list, colors, 0, {}, True, solutions)
i = 1
for solution in solutions:
    print("Solution " + str(i) + ": " + str(solution))
    i += 1
