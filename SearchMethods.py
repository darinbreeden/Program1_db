def breadth_first(start, end, adj, coords):
    source = start
    visited = []
    queue = []
    trip = []
    
    
    while source != end or len(visited) != len(coords):
        for i in range(0, len(trip)):
            visited.append(source)
            trip.append(source)
            for i in range(0, len(adj[source])):
                visited.append(adj[source[i]])
                trip.append(adj[source][i])
                if adj[source][i] == end:
                    return trip
            source = trip[i+1]
    print('No Route Found...')
            





def depth_first(start, end, adj, coords):
    print('Write this function.')
def ID_DFS(start, end, adj, coords):
    print('Write this function.')
def best_first(start, end, adj, coords):
    print('Write this function.')
def a_star(start, end, adj, coords):
    print('Write this function.')