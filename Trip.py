def menu(cities):
    city_start = ''
    city_end = ''
    while city_start not in cities:    
        city_start = input("Please enter city start: ")
        if city_start not in cities:
            print("City not found...")
    print(f'City start: {city_start}')
    while city_end not in cities:
        city_end = input("Please enter city destination: ")
        if city_end not in cities:
            print("City not found...")
    print(f'City end: {city_end}')
    trip = [city_start, city_end]
    return trip

def search_methods():
    print('Search Methods:')
    print('[a] breadth-first search')
    print('[b] depth-first search')
    print('[c] ID-DFS search')
    print('[d] best-first search')
    print('[e] A* search')
    user_selection = input('Please select a search method: ')
    if user_selection == 'a':
        print('breadth-first search selected...')
    if user_selection == 'b':
        print('depth-first search selected...')
    if user_selection == 'c':
        print('ID-DFS search selected...')
    if user_selection == 'd':
        print('best-first search selected...')
    if user_selection == 'e':
        print('A* search selected...')
    return user_selection

# class Trip():