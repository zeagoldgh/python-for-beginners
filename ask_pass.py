# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

passphrase_value = "sillygoose"
input_passphrase = ""

while input_passphrase != passphrase_value:
    input_passphrase = input("Enter Passphrase")

print("Login is successful!")