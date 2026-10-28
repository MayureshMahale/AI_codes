
import heapq

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

start = tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))

n = int(input("Enter number of obstacles: "))
obstacles = set()

for i in range(n):
    obstacles.add(tuple(map(int, input(f"Enter obstacle {i+1} (row col): ").split())))


# Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Possible movements
moves = [(-1, 0, "Up"), (1, 0, "Down"),
         (0, -1, "Left"), (0, 1, "Right")]


def a_star(start, goal):
    open_list = [(0, start)]
    cost = {start: 0}
    parent = {}
    visited = set()

    while open_list:
        f, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = []
            while current != start:
                previous, direction = parent[current]
                path.append((current, direction))
                current = previous

            path.append((start, "Start"))
            path.reverse()
            return path

        r, c = current

        for dr, dc, direction in moves:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if (0 <= nr < rows and 0 <= nc < cols
                and neighbor not in obstacles and neighbor not in visited):

                new_cost = cost[current] + 1

                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f_cost, neighbor))
                    parent[neighbor] = (current, direction)

    return None


# Run A*
path = a_star(start, goal)


# Display result
print("\n-----------------------------")
print("MODEL-BASED AGENT")
print("-----------------------------")

if path:
    print("\nAgent Navigation:")

    for i, (position, direction) in enumerate(path):
        print(f"Step {i+1}: Agent at {position}")

        if direction != "Start":
            print("Move:", direction)

    print("\nGoal Reached Successfully!")
    print("Path:")

    for position, direction in path:
        print(position, end=" -> ")

    print("Goal")

else:
    print("\nNo path found!")