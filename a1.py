def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

tiles = {
    "A": input("Enter Status of tile A (Dirty/Clean): ").capitalize(),
    "B": input("Enter Status of tile B (Dirty/Clean): ").capitalize(),
}
location = input("Enter Initial agent location (A/B): ").upper()

print("\nInitial State:")
print("Tile A:", tiles["A"])
print("Tile B:", tiles["B"])
print("Agent Location:", location)


if tiles["A"] == "Clean" and tiles["B"] == "Clean":
    print("\nBoth rooms are already clean!")

else:
    for step in range(1, 5):
        status = tiles[location]
        action = vacuum_agent(location, status)
        
        print("\nStep", step)
        print("percept:", [location, status])
        print("Action:", action)

        # Perform action
        if action == "Suck":
            tiles[location] = "Clean"
        elif action == "Right":
            location = "B"
        elif action == "Left":
            location = "A"

        print("Tile A:", tiles["A"])
        print("Tile B:", tiles["B"])
        print("Agent Location:", location)


        if tiles["A"] == "Clean" and tiles["B"] == "Clean":
            break

print("\nFinal State:")
print("Tile A:", tiles["A"])
print("Tile B:", tiles["B"])
print("Agent Location:", location)