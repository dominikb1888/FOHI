from collections import defaultdict
import sys
import json
import heapq
import netfuncs

def parse_routers(routers_data):
    """Parses the router data into a graph representation with adjacency lists."""
    graph = {}
    for router_ip, router_info in routers_data.items():
        if router_ip not in graph:
            graph[router_ip] = {}
        for neighbor_ip, connection in router_info['connections'].items():
            graph[router_ip][neighbor_ip] = connection['ad']  # use administrative distance as weight
    return graph

def dijkstras_shortest_path(routers: list, src_ip: str, dest_ip: str) -> list[str]:
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """
    # Find the appropriate routers for source and destination IPs
    src_router = netfuncs.find_router_for_ip(routers, src_ip)
    dest_router = netfuncs.find_router_for_ip(routers, dest_ip)

    # Check if either the source or destination is not in the graph
    if src_router is None or dest_router is None:
        return []

    # Convert router IPs to a useful graph format
    graph = parse_routers(routers)

    # Dijkstra's algorithm initialization
    min_heap = [(0, src_router, [])]  # (cumulative weight, node, path)
    visited = set()

    while min_heap:
        print(min_heap)

        current_weight, current_node, path = heapq.heappop(min_heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        # Path update with the current node
        current_path = path + [current_node]

        if current_node == dest_router:
            # Exclude the source and destination routers from the final path
            return current_path

        # Explore the neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (current_weight + weight, neighbor, current_path))

    # If no path is found, return an empty list
    return []

# Mocked data and testing segment (you'd typically have this in separate files)
if __name__ == "__main__":
    # Example usage with a test case
    with open("example1.json", "r") as f:
        data = json.load(f)
        routers_data = data['routers']

    src = "10.34.52.158"
    dest = "10.34.166.1"
    print(dijkstras_shortest_path(routers_data, src, dest))

#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

