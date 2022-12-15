with open('test.txt', 'r') as f:
    raw_input = f.read().splitlines()

sensors = {}
no_beacon = set()

DST_ROW = 10
MAX_COORDS = 20

for line in raw_input:
    sensor, beacon = line.split(':')
    sx, sy = [int(i.split('=')[1]) for i in sensor.split(',')]
    bx, by = [int(i.split('=')[1]) for i in beacon.split(',')]

    sensors[(sx, sy)] = (bx, by)

def dist(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)


for (sx, sy), (bx, by) in sensors.items():
    beacon_distance = dist((sx, sy), (bx, by)) 
    dst_distance = abs(sy - DST_ROW)
    if dst_distance > beacon_distance:
        continue
    row_len = beacon_distance - dst_distance
    for x in range(sx - row_len, sx + row_len + 1):
        if (x, DST_ROW) != (bx, by):
            no_beacon.add(x)

print(len(no_beacon))

# Part 2

# sensors = {sensor : dist(sensor, beacon) for sensor, beacon in sensor.items()}

