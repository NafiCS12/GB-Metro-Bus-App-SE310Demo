bus_lines = [
"Route 1 - Main Street",
"Route 3 - Webster Ave",
"Route 6 - Shawano Ave"
]

def show_all_buses():
    print("Available Bus Lines:")
    for bus in bus_lines:
        print(bus)

if __name__ == "__main__":
    show_all_buses()
