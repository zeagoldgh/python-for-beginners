# Write a script, where the user can enter a number. If the number is: 
#   - dividable by 3 print out "Fizz"
#   - dividable by 5 print out "Buzz"
#   - dividable by 3 & 5 print out "FizzBuzz"
#   - none of the above just print out the number

num = int(input("Give number!!!"))
fizz = num % 3
buzz = num % 5
if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 5 == 0:
    print("buzz")
elif num % 3 == 0:
    print("fuzz")
else: print(num)
