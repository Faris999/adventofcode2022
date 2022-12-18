with open('input.txt', 'r') as f:
    raw_input = f.read().splitlines()

coords = set(tuple(int(i) for i in line.split(',')) for line in raw_input)


def get_neighbors(coord):
    x, y, z = coord
    return [
        (x+1,y,z),
        (x-1,y,z),
        (x,y+1,z),
        (x,y-1,z),
        (x,y,z+1),
        (x,y,z-1)
    ]

def compute_surface_area(coords):

    graph = {coord: [i for i in get_neighbors(coord) if i in coords] for coord in coords}

    sides = 0

    for cube, neighbors in graph.items():
        sides += 6
        sides -= len(neighbors)

    return sides

surface_area = compute_surface_area(coords)
print(surface_area)

transposed = list(map(list, zip(*coords)))
min_coord = tuple(min(i)-1 for i in transposed)
max_coord = tuple(max(i)+1 for i in transposed)
print(min_coord, max_coord)

def inside_bounds(coord):
    return all(min_coord[i] <= coord[i] <= max_coord[i] for i in range(3))

def flood_fill(coord):
    filled = set()
    frontier = [coord]
    while len(frontier) > 0:
        current = frontier.pop(0)
        if current in coords:
            continue
        if not inside_bounds(current):
            continue
        filled.add(current)
        frontier.extend([i for i in get_neighbors(current) if i not in filled and inside_bounds(i) and i not in frontier])
    return filled

air_patches = []
airss = set()
outside = flood_fill(min_coord)
for x in range(min_coord[0]+1, max_coord[0]):
    for y in range(min_coord[1]+1, max_coord[1]):
        for z in range(min_coord[2]+1, max_coord[2]):
            if (x, y, z) in coords:
                continue
            if (x, y, z) in outside:
                continue
            if (x, y, z) in airss:
                continue
            airs = flood_fill((x, y, z))
            air_patches.append(airs)
            for air in airs:
                airss.add(air)


external_surface_area = surface_area

for airs in air_patches:
    external_surface_area -= compute_surface_area(airs)

print(external_surface_area)