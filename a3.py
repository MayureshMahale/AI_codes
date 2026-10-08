import heapq

# Calculate misplaced tiles (excluding blank 0)
def heuristic(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

# Generate valid neighbor states
def get_neighbors(state):
    b = state.index(0)
    r, c = b // 3, b % 3
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    
    neighbors = []
    for dr, dc, move in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nb = nr * 3 + nc
            s = list(state)
            s[b], s[nb] = s[nb], s[b]
            neighbors.append((tuple(s), move))
    return neighbors

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

def a_star(start, goal):
    # Priority Queue stores: (f_score, g_score, state, path)
    # path is a list of tuples: (state, move_taken)
    pq = [(heuristic(start, goal), 0, start, [(start, None)])]
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        # Goal Reached
        if current == goal:
            print("\n========== SOLUTION ==========\n")
            for step, (state, move) in enumerate(path):
                h = heuristic(state, goal)
                print("Step:", step)
                if step > 0:
                    print("Move:", move)
                print_puzzle(state)
                print("g(n) =", step)
                print("h(n) =", h)
                print("f(n) =", step + h)
                print("------------------------")
            print("Total moves:", len(path) - 1)
            return

        # Explore Neighbors
        for nxt_state, move in get_neighbors(current):
            if nxt_state not in visited:
                nxt_g = g + 1
                nxt_f = nxt_g + heuristic(nxt_state, goal)
                heapq.heappush(pq, (nxt_f, nxt_g, nxt_state, path + [(nxt_state, move)]))

    print("No solution found.")

# Inputs & Execution
print("Enter Initial State")
print("Enter 9 numbers separated by spaces (0 = blank):")
start = tuple(map(int, input().split()))

print("\nEnter Goal State")
print("Enter 9 numbers separated by spaces (0 = blank):")
goal = tuple(map(int, input().split()))

print("\n========== INITIAL STATE ==========")
print_puzzle(start)
print("\ng(n) =", 0)
print("h(n) =", heuristic(start, goal))
print("f(n) =", heuristic(start, goal))

a_star(start, goal)