#!/usr/bin/python3
# We can sort out lists using a number of ways in Python
cars = []
# We will use car brands in a dearlership as an example
cars.append("BMW")
cars.append("Nissan")
cars.append("Land Rover")
cars.append("Toyota")
cars.append("Audi")
cars.append("Mazda")

print(cars)
# We can check the length of the list as below
print(f"\nThe Number of Car Brands in the Dearlership is {len(cars)}\n")

# We can reverse the order without sorting alphabetically
cars.reverse()
print(cars)
# We can restore default order using the reverse function again
cars.reverse()
print(cars)

# Temporary sort is shown below
print(sorted(cars))
# We still have the original list as shown with the below print function
print(cars)

# Lastly we will sort out the list whose implications will be permanent
cars.sort()
print(cars)

# Reverse order of the sort can be attained by passing a parameter
cars.sort(reverse=True)
print(cars)