mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print("First Destination:", mission_route [0])
print("Final Destination:", mission_route [-1])
print("Total destinations:", len(mission_route))
print("Mission route:")

for destination in mission_route:
    print(destination)
if "Europa" in mission_route:
    print("Europa is a part on the mission route")
else:
    print("Europa is not a part on the mission route")

selected_destination = input("Enter a destination to search: ")
if selected_destination in mission_route:
    print(selected_destination, "is part of the mission's route")

    position = mission_route.index(selected_destination)
    print("Stops from start:", position)

    stops_from_end = len(mission_route) - 1 - position
    print("Stops from end:", stops_from_end)
    if position < len(mission_route) - 1:
        next_stop = mission_route[position + 1]
        print("Next stop:", next_stop)
    else:
        print("This is the final stop of the journey.")

else:
    print(selected_destination, "is not part of the mission's route")