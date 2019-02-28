#implement DFS 
def DFS(g, u, discovered):

    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)

# result = {u: None}
# DFS(g, u, result)

def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path

def DFS_complete(g):
    forest = { }
    for u i g.vertices():
        if u not in forest:
            forest[u] = None   #u will be the root of a tree
            DFS(g, u, forest)
    return forest
