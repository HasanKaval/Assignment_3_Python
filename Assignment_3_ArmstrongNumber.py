
number = input("Please enter your n-Armstrong number :  ")
while not(number.isnumeric()):
  number = input("Invalid entry! Please enter your number again :  ")
armstrong = 0
power = len(number)
for i in number:
  armstrong += int(i)**power
if armstrong == int(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")

