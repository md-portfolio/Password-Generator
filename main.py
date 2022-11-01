import random

#Obtain the desired lenght
passlen = (int(input("Enter the desired lenght of your password:")))

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" 

strongpass = "".join(random.sample(characters,passlen))

strongpasswordsuggestion = print(f"A strong password with {passlen} a password with 12 characters may be: {strongpass}")