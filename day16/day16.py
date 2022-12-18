with open('test.txt', 'r') as f:
    raw_input = f.read().splitlines()

class Valve():
    def __init__(self, name, flow_rate, neighbors) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors
        self.is_opened = False
    
    def __repr__(self) -> str:
        return f'{self.name} ({self.flow_rate}), connected to {",".join(self.neighbors)}'

valves = {}

for line in raw_input:
    valve, tunnels = line.split('; ')
    valve_name = valve.split(' ')[1]
    flow_rate = int(valve.split('=')[1])
    tunnels = tunnels.replace('valve', 'valves')[23:].split(', ')
    valves[valve_name] = Valve(valve_name, flow_rate, tunnels)

current_valve = 'AA'
