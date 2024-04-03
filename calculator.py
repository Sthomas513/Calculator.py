import math
#this function adds two numbers
def add(x, y):
    return x + y  
#this function subtracts two numbers  
def sustract(x, y):
    return x - y  
#this function multiplies two numbers
def multiply(x, y):  
    return x * y
#this function divides two numbers
def divide(x, y):
    return x / y
 #this function calculates the power of two numbers
def power(x, y):
    return x ** y
  #this function calculates the square root of a number
def square_root(x):
    return x ** 0.5
  #this function calculates the logarithm of a number
def logarithm(x):
    return math.log(x)
print("Select operation.")
print("1.Add")
print("2.Sustract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Square root")
print("7.Logarithm")
while True:
  choice = input("Enter choice(1/2/3/4/5/6/7): ")
  if choice in ('1', '2', '3', '4', '5', '6', '7'):
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      if choice == '1':
          print(num1, "+", num2, "=", add(num1, num2))
      elif choice == '2':
          print(num1, "-", num2, "=", sustract(num1, num2))
      elif choice == '3':
          print(num1, "*", num2, "=", multiply(num1, num2))
      elif choice == '4':
          print(num1, "/", num2, "=", divide(num1, num2))
      elif choice == '5':
          print(num1, "**", num2, "=", power(num1, num2))
      elif choice == '6':
          print("Square root of", num1, "=", square_root(num1))
      elif choice == '7':
          print(num1, "log", num2, "=", logarithm(num1))
      # check if user wants another calculation
      # break the while loop if answer is no
      next_calculation = input("Let's do next calculation? (yes/no): ")
      if next_calculation == "no":
          break   
  else:
      print("Invalid Input")  
