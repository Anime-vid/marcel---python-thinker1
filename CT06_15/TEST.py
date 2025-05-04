# num = 10
# while num != 210:
#     print(num)
#     num += 10
# 1. Write code below to print the 3rd item 
#    in this list using index e.g. earth
planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
print(planets[3])
# 2. Write code to append neptune to this list.
planets.append("neptune")
#    Rename Mars in the list to be "muskworld"
planets[3] = "muskworld"
planets.pop(6)
# 4. Remove uranus from this list.
# 5. Using a for loop, print all the planets  from this list one by one.
counter = 0
for i in range(counter):
    print(planets[i])
    counter = counter + 1