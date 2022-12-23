## missspelled 

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
print(drivers)

## Add another name

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
print(drivers)

# What's this? There's another group of drivers that comes out of nowhere to join the race! Add each element from the others list to the end of the drivers list.
others = ["Blue", "Elton", "Thomas"]

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
print(drivers)

# Thomas looks lost out there! He has a horrible fiery crash.  Remove the last element from the drivers list ("Thomas")


drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
drivers.remove("Thomas")
print(drivers)

# Oh dear, there's a huge crash at the front! Remove the first element from the driver's list

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
drivers.remove("Thomas")
drivers.remove("Charles")
print(drivers)


# And again the leader of the pack runs into trouble! He's not out of the race, but he's now moved to last place.  Remove the first driver in the list, store it in variable, and then add it to the end of the list.

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
drivers.remove("Thomas")
drivers.remove("Charles")
drivers.remove("Pierre")
drivers.insert(7, "Pierre")
print(drivers)

# My idiotic cat, Blue, is in the middle of the pack.  Delete "Blue" from the drivers list using the remove method!

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
drivers.remove("Thomas")
drivers.remove("Charles")
drivers.remove("Pierre")
drivers.insert(7, "Pierre")
drivers.remove("Blue")
print(drivers)


# My dog, Elton, is making a remarkable charge up the leadboard! Remove Elton from his current position in the list and insert him at index 2.

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
drivers.remove("Thomas")
drivers.remove("Charles")
drivers.remove("Pierre")
drivers.insert(7, "Pierre")
drivers.remove("Blue")
drivers.remove("Elton")
drivers.insert(2, "Elton")
print(drivers)

# The race is over! It's time for the podium ceremony.  Create a new list called podium that contains the first 3 elements from the drivers list. (use a slice!)
drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
drivers.remove("Thomas")
drivers.remove("Charles")
drivers.remove("Pierre")
drivers.insert(7, "Pierre")
drivers.remove("Blue")
drivers.remove("Elton")
drivers.insert(2, "Elton")
podium = drivers[0:3]
for driver in podium:
    print(driver)

    # Loop over the drivers list and print out a leadboard that includes a driver's finishing position and their name, like this:

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtterri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Thomas"])
drivers.remove("Thomas")
drivers.remove("Charles")
drivers.remove("Pierre")
drivers.insert(7, "Pierre")
drivers.remove("Blue")
drivers.remove("Elton")
drivers.insert(2, "Elton")
podium = drivers[0:3]
for drivers in podium:
    print(drivers)

# Loop over the drivers list and print out a leadboard that includes a driver's finishing position and their name, like this:


counter = 1
for driver in drivers:
    print(str(counter) + ", " + driver)
    counter += 1

for num, name in enumerate(drivers, start = 1):
    print(str(num) + ". " + name)