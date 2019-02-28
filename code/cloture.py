from copy import deepcooy
def floyd_washall (g):
    closure = deepcooy(g)
    verts = list(closure.vertices())
    n = len(verts)
    for k in range(n):
        for i in range(n):
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    if i!= != j != k and closure.get_edge(verts[i], verts[j]) is not None:
                        closure.insert_edge(verts[i], verts[j])
    return closure