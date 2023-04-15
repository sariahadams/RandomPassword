import random
#randomizes

char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
#string of characters to create the randomized password

password = int(input("Enter length of password (8-14 characters) : "))
#waits for user input 

while password < 8 or password > 14:
  print("Invaild length. Please enter a number between 8 and 14.")

  password = int(input("Enter length of password (8-14 characters) : "))

#length between 8 and 14 allowed only to ensure the randomized password isn't too long but also not too short. Replays message if input doesn't follow requirements

join = "".join(random.sample(char, password))

print(join)
#creates randomized password and prints it
