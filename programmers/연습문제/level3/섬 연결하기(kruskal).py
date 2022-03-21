def solution(n, costs):
    # Find the root node of x recursively.
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # Union the two sets.
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [0] * n
    for i in range(n):
        parent[i] = i

    result = 0
    costs.sort(key = lambda x : x[-1])

    # Check in order of low-cost edges.
    for edge in costs:
        a, b, cost = edge
        # If there will be no cycle, union.
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    return result