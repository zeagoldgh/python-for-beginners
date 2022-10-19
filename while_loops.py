# Write a while loop that prints the even numbers from 100 to 140 (including 140)

number = 100

while number <=140:
  if(number % 2 == 0):
    print(number)
  number = number + 1


# Write a for loop that does the same thing (with range())

numbers = range(100, 141, 2)
for number in numbers:
    print(number)