from collections import deque

# BFS function
def bfs(start, goal):

    queue = deque([(start, [])])
    visited = {start}

    level = 0

    while queue:

        print("\n========== LEVEL", level, "==========")

        # Process all states at current level
        for _ in range(len(queue)):

            state, path = queue.popleft()

            print("\nState:")

            print(state[0], state[1], state[2])
            print(state[3], state[4], state[5])
            print(state[6], state[7], state[8])

            # Check goal
            if state == goal:

                print("\nGoal Found!")

                return path


            # Find blank position
            zero = state.index(0)

            row = zero // 3
            col = zero % 3


            # Possible moves
            moves = [
                (-1, 0, "UP"),
                (1, 0, "DOWN"),
                (0, -1, "LEFT"),
                (0, 1, "RIGHT")
            ]


            # Generate next states
            for dr, dc, move in moves:

                nr = row + dr
                nc = col + dc

                if 0 <= nr < 3 and 0 <= nc < 3:

                    new_zero = nr * 3 + nc

                    new_state = list(state)

                    # Swap blank with next tile
                    new_state[zero], new_state[new_zero] = \
                        new_state[new_zero], new_state[zero]

                    new_state = tuple(new_state)


                    # Add new state if not visited
                    if new_state not in visited:

                        visited.add(new_state)

                        queue.append(
                            (new_state, path + [move])
                        )


        level += 1


    return None


# Take 3x3 grid input
def get_grid_input(prompt):

    print(prompt)

    grid = []

    for i in range(3):

        row = list(map(int, input().split()))

        grid.extend(row)

    return tuple(grid)


# Input
start = get_grid_input(
    "Enter Initial State (3 rows, 0 for blank):"
)

goal = get_grid_input(
    "Enter Goal State (3 rows):"
)


# Run BFS
solution = bfs(start, goal)


# Display solution
if solution:

    print("\nSolution:")

    print(" -> ".join(solution))

    print("Total moves:", len(solution))

else:

    print("\nNo solution exists.")