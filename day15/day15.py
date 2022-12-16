from typing import Iterable, Self

with open('input.txt', 'r') as f:
    raw_input = f.read().splitlines()

sensors = {}
no_beacon = set()

DST_ROW = 2000000
MAX_COORDS = 4000000
class ClosedInterval():
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper
        self.length = upper - lower
        self.size = upper - lower + 1

    def intersects(self, other):
        return self.upper >= other.lower and other.upper >= self.lower

    def combinable(self, other):
        return self.intersects(other) or max(self.lower, other.lower) - min(self.upper, other.upper) == 1

    def union(self, other):
        if self.combinable(other):
            return ClosedInterval(min(self.lower, other.lower), max(self.upper, other.upper))
        return tuple(sorted([self, other], key=lambda x: x.lower))

    def intersection(self, other):
        if not self.intersects(other):
            return None
        return(ClosedInterval(max(self.lower, other.lower), min(self.upper, other.upper)))

    def __contains__(self, other):
        # Other contained in self
        if isinstance(other, ClosedInterval):
            return other.lower >= self.lower and other.upper <= self.upper
        if isinstance(other, int):
            return self.lower <= other <= self.upper
        raise NotImplemented

    def __sub__(self, other):
        if not self.intersects(other):
            return self
        if self in other:
            return None
        intersection = self.intersection(other)
        if self.lower == intersection.lower:
            return ClosedInterval(intersection.upper + 1, self.upper)
        if self.upper == intersection.upper:
            return ClosedInterval(self.lower, intersection.lower - 1)
        if other in self:
            return (ClosedInterval(self.lower, other.lower-1), ClosedInterval(other.upper+1, self.upper))

    def __eq__(self, __o: object) -> bool:
        return self.lower == __o.lower and self.upper == __o.upper

    def __hash__(self) -> int:
        return hash((self.lower, self.upper))

    def __repr__(self) -> str:
        return f'[{self.lower},{self.upper}]'
    
    def __lt__(self, other):
        return self.lower < other.lower


def combine_all(intervals: Iterable[ClosedInterval]):
    if len(intervals) <= 2:
        return intervals
    intervals = list(sorted(intervals))
    new_intervals = []
    i = 0
    current_interval = intervals[i]
    while i < len(intervals)-1:
        if current_interval.combinable(intervals[i+1]):
            current_interval = current_interval.union(intervals[i+1])
        else:
            new_intervals.append(current_interval)
            current_interval = intervals[i+1]
        i += 1
    new_intervals.append(current_interval)
    return new_intervals


for line in raw_input:
    sensor, beacon = line.split(':')
    sx, sy = [int(i.split('=')[1]) for i in sensor.split(',')]
    bx, by = [int(i.split('=')[1]) for i in beacon.split(',')]

    sensors[(sx, sy)] = (bx, by)

intervals = set() 

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
    interval = ClosedInterval(sx - row_len, sx + row_len)
    if by == DST_ROW:
        interval -= ClosedInterval(bx, bx)
    if isinstance(interval, tuple):
        for i in interval:
            intervals.add(i)
    elif interval is not None:
        intervals.add(interval)

# print(len(no_beacon))
print(sum(interval.size for interval in combine_all(intervals)))

# Part 2

sensors = {sensor : dist(sensor, beacon) for sensor, beacon in sensors.items()}

found_beacon = None

for y in range(MAX_COORDS+1):
    intervals = set()
    for (sx, sy), beacon_distance in sensors.items():
        dst_distance = abs(sy - y)
        if dst_distance > beacon_distance:
            continue
        row_len = beacon_distance - dst_distance
        interval = ClosedInterval(max(0, sx - row_len), min(MAX_COORDS, sx + row_len))
        intervals.add(interval)
    intervals = combine_all(intervals)
    if len(intervals) != 1:
        found_beacon = intervals[0].upper+1, y
        break

print(found_beacon[0]*4000000 + found_beacon[1])