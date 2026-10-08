n = int(input("Enter number of cities: "))

cities = []

for i in range(n):
    cities.append(input(f"Enter city {i + 1}: ").upper())


# Store distances
dist = {}

print("\nEnter distances between cities (-1 for no connection):")

for city1 in cities:

    dist[city1] = {}

    for city2 in cities:

        if city1 == city2:
            dist[city1][city2] = 0

        elif city2 in dist and city1 in dist[city2]:
            dist[city1][city2] = dist[city2][city1]

        else:
            dist[city1][city2] = int(
                input(f"Distance {city1} -> {city2}: ")
            )


k = int(input("\nEnter beam width (k): "))
start = input("Enter starting city: ").upper()


# Calculate cost
def cost(path):

    total = 0

    for i in range(len(path) - 1):

        d = dist[path[i]][path[i + 1]]

        if d == -1:
            return 999999

        total += d

    return total


# Initial beam
beam = []

for city in cities:

    if city != start and dist[start][city] != -1:
        beam.append([start, city])


beam.sort(key=cost)
beam = beam[:k]


print("\nInitial Beam:")

for path in beam:
    print(path, "Cost =", cost(path))


# Beam Search
while beam and len(beam[0]) < len(cities):

    candidates = []

    for path in beam:

        for city in cities:

            if city not in path:

                if dist[path[-1]][city] != -1:

                    new_path = path + [city]

                    candidates.append(new_path)


    candidates.sort(key=cost)

    beam = candidates[:k]


    print("\nCurrent Beam:")

    for path in beam:
        print(path, "Cost =", cost(path))


# Find best tour
best_tour = None
best_cost = 999999

for path in beam:

    last_city = path[-1]

    if dist[last_city][start] != -1:

        total_cost = cost(path) + dist[last_city][start]

        if total_cost < best_cost:

            best_cost = total_cost
            best_tour = path + [start]


# Display result
if best_tour:

    print("\nBest Tour:")
    print(" -> ".join(best_tour))

    print("Total Distance =", best_cost)

else:

    print("\nNo complete tour possible.")