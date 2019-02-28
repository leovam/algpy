def BFS(g, s, discovered):
    level =[s]
    while len(level) > 0:
        next_level =[]
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level
        