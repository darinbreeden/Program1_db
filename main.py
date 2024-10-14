from Trip import *
from Functions import *
from SearchMethods import *

coords = []
adj = {}
cities = []

readCSV("coordinates (1).csv", coords)
readTXT("Adjacencies.txt", adj)

for i in range(0,len(coords)):
    cities.append(coords[i][0])

print('Accessing Menu...')
trip = menu(cities)
print('Accessing Search Methods...')
user_selection = search_methods()
if user_selection == 'a':
    trip_total = breadth_first(trip[0], trip[1], adj, coords)
if user_selection == 'b':
    trip_total = depth_first(trip[0], trip[1], adj, coords)
if user_selection == 'c':
    trip_total = ID_DFS(trip[0], trip[1], adj, coords)
if user_selection == 'd':
    trip_total = best_first(trip[0], trip[1], adj, coords)
if user_selection == 'e':
    trip_total = a_star(trip[0], trip[1], adj, coords)

if len(trip_total) != 0:
    print('Total Trip:')
    for i in len(trip_total):
        print(f'\t[{i+1}] {trip_total[i]}')
