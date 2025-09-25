import sys

# read the graph edges from file


def load_graph(filename):
    graph = {}
    nodes = set()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # skip empty or comment
                continue
            u, v = line.split()
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            nodes.add(u)
            nodes.add(v)
    # make sure all nodes are in the dict
    for n in nodes:
        if n not in graph:
            graph[n] = []
    return graph, sorted(list(nodes))

# DFS to collect cycles


def find_cycles(graph, nodes):
    cycles = []

    # recursive dfs
    def dfs(start, current, visited):
        visited.add(current)
        path.append(current)
        for nxt in graph[current]:
            if nxt < start:   # to avoid duplicate cycles
                continue
            if nxt == start:
                cycles.append(path[:])   # found a cycle
            elif nxt not in visited:
                dfs(start, nxt, visited)
        path.pop()
        visited.remove(current)

    # try dfs from each node
    for start in nodes:
        path = []
        dfs(start, start, set())

    return cycles

# make cycle into nice string


def format_cycle(c):
    return " -> ".join(c + [c[0]])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("need input file: python main.py file.txt")
        sys.exit(1)

    fname = sys.argv[1]
    g, nodes = load_graph(fname)
    found = find_cycles(g, nodes)

    # remove duplicates if any
    uniq = []
    seen = set()
    for c in found:
        t = tuple(c)
        if t not in seen:
            seen.add(t)
            uniq.append(c)

    if not uniq:
        print("No deadlocks found.")
    else:
        print("Total deadlock cycles:", len(uniq))
        for i, cyc in enumerate(uniq, 1):
            print("Cycle", i, ":", format_cycle(cyc))
