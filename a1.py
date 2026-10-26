
def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Right"
    elif location == "C":
        return "Right"
    elif location == "D":
        return "Left"


tiles = {
    "A": input("Enter Status of tile A (Dirty/Clean): ").capitalize(),
    "B": input("Enter Status of tile B (Dirty/Clean): ").capitalize(),
    "C": input("Enter Status of tile C (Dirty/Clean): ").capitalize(),
    "D": input("Enter Status of tile D (Dirty/Clean): ").capitalize()
}

location = input("Enter Initial agent location (A/B/C/D): ").upper()

print("\nInitial State:")
for tile in tiles:
    print("Tile", tile + ":", tiles[tile])

print("Agent Location:", location)


if all(status == "Clean" for status in tiles.values()):
    print("\nAll rooms are already clean!")

else:
    for step in range(1, 20):
        status = tiles[location]
        action = vacuum_agent(location, status)

        print("\nStep", step)
        print("Percept:", [location, status])
        print("Action:", action)

        # Perform action
        if action == "Suck":
            tiles[location] = "Clean"
        elif action == "Right":
            if location == "A":
                location = "B"
            elif location == "B":
                location = "C"
            elif location == "C":
                location = "D"
        elif action == "Left":
            location = "C"

        for tile in tiles:
            print("Tile", tile + ":", tiles[tile])

        print("Agent Location:", location)

        if all(status == "Clean" for status in tiles.values()):
            break

print("\nFinal State:")
for tile in tiles:
    print("Tile", tile + ":", tiles[tile])

print("Agent Location:", location)
