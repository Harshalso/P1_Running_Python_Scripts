cities = ["Pune", "Mumbai", "Nagpur"]
print(type(cities))

cities.append("Raver")

cities.insert(1, "Delhi")

print(cities)
cities.pop()
cities.pop(1)
print(cities)

for city in cities:
    print("The current value is:")
    print(city)

print("Process completed")
