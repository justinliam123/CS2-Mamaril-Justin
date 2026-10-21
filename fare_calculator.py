# Travel Fare Calculator
FARE_RATE = 14

while True:
    name = input("Enter passenger name: ")

    if name.strip() != "":
        break # Stops the loop once a valid name is entered.
    else:
        print("Invalid name. Name cannot be empty.")

while True:
    distance = input("Enter distance (km): ")

    if distance.replace('.', '', 1).isdigit() and float(distance) > 0:
        distance = float(distance)
        break # Stops the loop once a valid input is entered.
    else:
        print("Invalid distance. Enter a number greater than 0.")

while True:
    passengers = input("Enter number of passengers: ")

    if passengers.isdigit() and int(passengers) > 0:
        passengers = int(passengers)
        break # Stops the loop once a valid input is entered.
    else:
        print("Invalid passengers. Enter a positive whole number.")

# Calculate total fare
total_fare = distance * FARE_RATE * passengers

# Display output
print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
