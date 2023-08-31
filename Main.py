from graph import Graph

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    g = Graph()

    n = get_integer_input("Edges: ")
    for _ in range(n):
        u = input("From: ")
        v = input("To: ")
        w = get_integer_input("Weight: ")
        g.add_edge(u, v, w)

    start = input("Start: ")
    dists = g.dijkstra(start)

    print("Shortest distances from", start)
    for v, d in dists.items():
        print("To", v + ":", d)

if __name__ == "__main__":
    main()

