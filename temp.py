def function_1_represent_network():
    """
    1. Representing the flow network (Pre-defined).
    Initializes the capacity and flow matrices.
    """
    num_vertices = 6
    source = 0
    sink = 5

    # Initialize capacity and flow matrices with zeros
    capacity = [[0] * num_vertices for _ in range(num_vertices)]
    flow = [[0] * num_vertices for _ in range(num_vertices)]

    # Pre-defined edges (u, v, capacity)
    edges = [
        (0, 1, 16),
        (0, 2, 13),
        (1, 2, 10),
        (1, 3, 12),
        (2, 1, 4),
        (2, 4, 14),
        (3, 5, 20),
        (4, 5, 4),
    ]

    for u, v, cap in edges:
        capacity[u][v] = cap

    print("1(d) Input Network:")
    for u in range(num_vertices):
        for v in range(num_vertices):
            if capacity[u][v] > 0:
                print(f"{u} -> {v}: {capacity[u][v]}")

    return capacity, flow, num_vertices, source, sink


def function_2_find_augmenting_path(capacity, flow, source, sink, num_vertices):
    """
    2. Finding an augmenting path and printing residual capacities.
    """
    print("\n2(a) Current Residual Graph Capacities:")
    for u in range(num_vertices):
        for v in range(num_vertices):
            if capacity[u][v] > 0:
                res_forward = capacity[u][v] - flow[u][v]
                if res_forward > 0:
                    print(f"  Forward  {u} -> {v}: {res_forward}")
                if flow[u][v] > 0:
                    print(f"  Backward {v} -> {u}: {flow[u][v]}")

    # 2(b) BFS traversal to find augmenting path
    parent = [-1] * num_vertices
    parent[source] = source
    queue = [source]
    found = False

    while queue:
        u = queue.pop(0)
        if u == sink:
            found = True
            break

        for v in range(num_vertices):
            # Forward edge condition: capacity exists, unvisited, and flow < capacity
            if capacity[u][v] > 0 and parent[v] == -1 and flow[u][v] < capacity[u][v]:
                parent[v] = u
                queue.append(v)
            # Backward edge condition: reverse capacity exists, unvisited, and flow > 0
            elif capacity[v][u] > 0 and parent[v] == -1 and flow[v][u] > 0:
                parent[v] = u
                queue.append(v)

    # 2(c) Print the augmenting path found
    if found:
        path = []
        curr = sink
        while curr != source:
            path.insert(0, curr)
            curr = parent[curr]
        path.insert(0, source)
        print(f"\n2(c) Augmenting Path found: {' -> '.join(map(str, path))}")

        # 2(d) Print residual capacities along the specific path
        print("2(d) Residual capacities along this path:")
        curr = sink
        while curr != source:
            p = parent[curr]
            if capacity[p][curr] > 0:
                print(f"  {p} -> {curr}: {capacity[p][curr] - flow[p][curr]}")
            else:
                print(f"  {curr} -> {p} (backward): {flow[curr][p]}")
            curr = p

    return found, parent


def function_3_augment_flow(capacity, flow, parent, source, sink):
    """
    3. Augmenting the flow along the path.
    """
    # 3(a) Determine bottleneck capacity
    b = float("inf")
    curr = sink
    while curr != source:
        p = parent[curr]
        if capacity[p][curr] > 0:  # Forward edge
            b = min(b, capacity[p][curr] - flow[p][curr])
        else:  # Backward edge
            b = min(b, flow[curr][p])
        curr = p

    print(f"\n3(a) Bottleneck Capacity: {b}")

    # 3(b) & (c) Update flow
    print("3(d) Updated flow on affected edges:")
    curr = sink
    while curr != source:
        p = parent[curr]
        if capacity[p][curr] > 0:  # Forward edge
            flow[p][curr] += b
            print(
                f"  Increased forward edge {p}->{curr} to {flow[p][curr]}/{capacity[p][curr]}"
            )
        else:  # Backward edge
            flow[curr][p] -= b
            print(
                f"  Decreased backward edge {curr}->{p} to {flow[curr][p]}/{capacity[curr][p]}"
            )
        curr = p

    return b


def function_4_compute_max_flow():
    """
    4. Computing the maximum flow by repeatedly finding paths and augmenting.
    """
    print("=== STARTING MAXIMUM FLOW COMPUTATION ===")

    # 4 Initialize the network
    capacity, flow, num_vertices, source, sink = function_1_represent_network()

    max_flow = 0
    iteration = 1

    # 4(a) Repeatedly search for paths in the residual graph
    while True:
        print(f"\n--- Iteration {iteration} ---")

        found, parent = function_2_find_augmenting_path(
            capacity, flow, source, sink, num_vertices
        )

        # 4(c) Stop when no path found
        if not found:
            print("\nNo more augmenting paths found. Terminating.")
            break

        # 4(b) Update flow
        flow_added = function_3_augment_flow(capacity, flow, parent, source, sink)
        max_flow += flow_added

        print(f"\n4(d) Flow added in Iteration {iteration}: {flow_added}")
        iteration += 1

    # 4(d) Print final results
    print("\n=================================")
    print(f"4(d) TOTAL MAXIMUM FLOW: {max_flow}")
    print("=================================")

    print("\n4(d) Final Flow along each edge:")
    for u in range(num_vertices):
        for v in range(num_vertices):
            if capacity[u][v] > 0:
                if flow[u][v] > 0:
                    print(f"{u} -> {v}: {flow[u][v]}/{capacity[u][v]}")


# ==========================================
# DRIVER CODE: Executing the Numbered Functions
# ==========================================

print("=== DEMONSTRATING INDIVIDUAL CALLS (SINGLE ITERATION) ===")

# 1. Call Function 1 to initialize and get the network data
cap, fl, n_v, src, snk = function_1_represent_network()

# 2. Call Function 2 to find the first augmenting path
found_path, parent_arr = function_2_find_augmenting_path(cap, fl, src, snk, n_v)

# 3. Call Function 3 to augment the flow for that specific path
if found_path:
    function_3_augment_flow(cap, fl, parent_arr, src, snk)


print("\n\n" + "=" * 50)
print("=== EXECUTING FULL ALGORITHM (FUNCTION 4) ===")
print("=" * 50 + "\n")

# 4. Call Function 4 to run the complete, automated process.
function_4_compute_max_flow()
