bus_lines = [
    "Route 1 - Main Street",
    "Route 3 - Webster Ave",
    "Route 6 - Shawano Ave"
]

favorites = []

def show_all_buses():
    print("Available Bus Lines:")
    for bus in bus_lines:
        print(bus)

def search_bus(route_name):
    results = [bus for bus in bus_lines if route_name.lower() in bus.lower()]
    print("Search Results:")
    for bus in results:
        print(bus)

def add_favorite(bus):
    favorites.append(bus)
    print(f"{bus} added to favorites")

if __name__ == "__main__":
    show_all_buses()
    search_bus("Route 3")   # keep feature/search-bus contribution
    add_favorite("Route 1 - Main Street")
