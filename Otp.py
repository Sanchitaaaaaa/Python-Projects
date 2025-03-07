import random
generatorotp = random.randint(000000, 100000)
username = input("Username : ")
print('Hello ! ', username)
print("Here's your otp to login : ", generatorotp)
password = input("Enter the otp to login : ")
if password == str(generatorotp):
    print("Login Successful ")
else:
    print("Login failed")
