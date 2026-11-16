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