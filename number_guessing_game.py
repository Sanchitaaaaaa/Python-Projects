import random

number = random.randint(1,99)
while True:
  try:
      num = int(input("Enter a number between 1 - 100 "))

      if(num < number):
          print("too low")
      elif (num > number):
          print("too high")
      else:
          print("you won! the right number is ", number)
          break
  except ValueError:
      print("error!!")





