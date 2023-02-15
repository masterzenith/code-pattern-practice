"""
Airport Connections
For the purpose of this question, the phrases "airport route" and "airport connection" are used interchangeably.
You're given a list of airports (three-letter codes like "JFK"), a list of routes (one-way flights from one airport to
another like ["JFK", "SFO"]), and a starting airport.
Write a function that returns the minimum number of airport connections (one-way flights) that need to be added in order
for someone to be able to reach any airport in the list, starting at the starting airport.
Note that routes only allow you to fly in one direction; for instance, the route ["JFK", "SFO"] only allows you to fly
from "JFK" to "SFO".
Also note that the connections don't have to be direct; it's okay if an airport can only be reached from the starting
airport by stopping at other airports first.
Sample Input:
airports = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
    "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD",
]

routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"],
]

startingAirport = "LGA"

Sample Output:
3 // ["LGA", "TLV"], ["LGA", "SFO"], and ["LGA", "EWR"]

Hints:
1. Start by creating a graph out of the inputs. Each airport should be a vertex in the graph, and each route should be
an edge. The graph should be directed with potential cycles, since it's possible for there to be round-trip flights
between airports or for some series of flights to eventually lead back to an arbitrary starting point. How can this graph
be useful?
2. Using the graph mentioned in Hint #1, try getting all of the airports that are unreachable from the starting airport.
This can be done using depth-first search. Is the number of unreachable airports the answer? If not, what extra information
do you need to get to the answer?
3. A single unreachable airport could have connections to a bunch of other unreachable airports, potentially making it
more "valuable", since adding one connection to it would make many other airports reachable.
4. Calculate the number of unreachable airports that are reachable from each unreachable airport (this can be done using
depth-first search), sort them in descending order according to this number, and count the minimum number of connections
that need to be added by iterating through this sorted list of unreachable airports, removing every unreachable airport's
unreachable connections as you go through the list.

Optimal Space & Time Complexity
O(a * (a + r) + a + r + alog(a)) time | O(a + r) space - where a is the number of airports and r is the number of routes

https://github.com/lee-hen/Algoexpert/tree/master/very_hard/22_airport_connections#hints
"""


class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.is_reachable = True
        self.unreachable_connections = []


def airport_connections(airports, routes, starting_airport):
    airport_graph = create_airport_graph(airports, routes)
    # print(airport_graph)
    unreachable_airport_nodes = get_unreachable_airport_nodes(airport_graph, airports, starting_airport)
    mark_unreachable_connections(airport_graph, unreachable_airport_nodes)
    return get_min_number_of_new_connections(airport_graph, unreachable_airport_nodes)


def create_airport_graph(airports, routes):
    airport_graph = {}
    for airport in airports:
        airport_graph[airport] = AirportNode(airport)
    for route in routes:
        airport, connection = route
        airport_graph[airport].connections.append(connection)
    return airport_graph


def get_unreachable_airport_nodes(airport_graph, airports, starting_airport):
    visited_airports = {}
    dfs_traverse_airports(airport_graph, starting_airport, visited_airports)

    unreachable_airport_nodes = []
    for airport in airports:
        if airport in visited_airports:
            continue
        airport_node = airport_graph[airport]
        airport_node.is_reachable = False
        unreachable_airport_nodes.append(airport_node)
    return unreachable_airport_nodes


def dfs_traverse_airports(airport_graph, airport, visited_airports):
    if airport in visited_airports:
        return

    visited_airports[airport] = True
    connections = airport_graph[airport].connections
    for connection in connections:
        dfs_traverse_airports(airport_graph, connection, visited_airports)


def mark_unreachable_connections(airport_graph, unreachable_airport_nodes):
    for airport_node in unreachable_airport_nodes:
        airport = airport_node.airport
        unreachable_connections = []
        dfs_first_add_unreachable_connections(airport_graph, airport, unreachable_connections, {})
        airport_node.unreachable_connections = unreachable_connections


def dfs_first_add_unreachable_connections(airport_graph, airport, unreachable_connections, visited_airports):
    if airport_graph[airport].is_reachable:
        return
    if airport in visited_airports:
        return

    visited_airports[airport] = True
    unreachable_connections.append(airport)
    connections = airport_graph[airport].connections
    for connection in connections:
        dfs_first_add_unreachable_connections(airport_graph, connection, unreachable_connections, visited_airports)


def get_min_number_of_new_connections(airport_graph, unreachable_airport_nodes):
    unreachable_airport_nodes.sort(key=lambda airport: len(airport.unreachable_connections), reverse=True)
    number_of_new_connections = 0
    for airport_node in unreachable_airport_nodes:
        if airport_node.is_reachable:
            continue
        number_of_new_connections += 1
        for connection in airport_node.unreachable_connections:
            airport_graph[connection].is_reachable = True
    return number_of_new_connections


def main():
    airports = [
        "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
        "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD",
    ]

    routes = [
        ["DSM", "ORD"],
        ["ORD", "BGI"],
        ["BGI", "LGA"],
        ["SIN", "CDG"],
        ["CDG", "SIN"],
        ["CDG", "BUD"],
        ["DEL", "DOH"],
        ["DEL", "CDG"],
        ["TLV", "DEL"],
        ["EWR", "HND"],
        ["HND", "ICN"],
        ["HND", "JFK"],
        ["ICN", "JFK"],
        ["JFK", "LGA"],
        ["EYW", "LHR"],
        ["LHR", "SFO"],
        ["SFO", "SAN"],
        ["SFO", "DSM"],
        ["SAN", "EYW"],
    ]

    startingAirport = "LGA"

    print(airport_connections(airports, routes, startingAirport))


if __name__ == "__main__":
    main()
