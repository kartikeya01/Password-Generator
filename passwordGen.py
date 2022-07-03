import random

u_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*._-"

Use_for = l_case + u_case + numbers + symbols

# length of the required password(change as per requirement)
length_for_pass = 8

password = "".join(random.sample(Use_for, length_for_pass))
print("Generated Password: " + password)
