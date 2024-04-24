import sys
import json
import math  # If you want to use math.inf for infinity

import netfuncs

def dijkstras_shortest_path(routers, src_ip, dest_ip):
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

    """
    - Weise allen Knoten die beiden Eigenschaften (Attribute) „Distanz“ und „Vorgänger“ zu. Initialisiere die Distanz im Startknoten mit 0 und in allen anderen Knoten mit ∞.
    - Solange es noch unbesuchte Knoten gibt, wähle darunter denjenigen mit minimaler (aufsummierter) Distanz aus und Speichere, dass dieser Knoten schon besucht wurde.
    - Berechne für alle noch unbesuchten Nachbarknoten die Gesamtdistanz des Pfades über die Summe des jeweiligen  Kantengewichtes und der bereits berechneten Distanz des Pfades vom Startknoten zum aktuellen Knoten.
    - Ist dieser Wert für einen Knoten kleiner als die dort gespeicherte bisherige aufsummierte Distanz des Pfades, aktualisiere sie und setze den aktuellen Knoten als Vorgänger. Dieser Schritt wird auch als Update oder Relaxation/Relaxierung bezeichnet.
    """

    rlist = {}
    for router_ip, config in routers.items():
        if netfuncs.ips_same_subnet(src_ip, dest_ip, config['netmask']):
            return []

        if router_ip == src_ip:
            rlist[router_ip] = {'dist': 0, 'config': config, 'prev': None)
        else:
            rlist[router_ip] = {'dist': math.inf, 'config': config, 'prev': None)

    path = []
    while rlist:
        for ip, values in rlist.items:

            next = next(sort_connections(values['config']))
            if values['dist'] == math.inf and next:
                rlist[ip]['dist'] += next['ad']



                if CONDITION: # distance between current sum of path is bigger than existing path cumsums
                    rlist.pop(router_ip, None) # remove router ip from rlist
            else:

    return path

def sort_connections(config: dict):
    """ Returns a Generator of sorted connections of a route """
    return sorted(config, lambda x: x['ad'])

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

