from replit import clear
from art import logo

def addition(n1, n2):
  return n1 + n2

def subtraction(n1,n2):
  return n1 - n2

def multiplication(n1,n2):
  return n1 * n2

def division(n1,n2):
  return n1 / n2

operations = {
  "+" : addition,
  "-" : subtraction,
  "*" : multiplication,
  "/" : division
}

def calculator():
  print(logo)
  number1 = float(input("What's the first number?: "))
  for symbols in operations.keys():
    print(symbols)
  continuation = True

  while continuation == True:
    operation = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    operation_selected = operations[operation]
    answer = operation_selected(number1, number2)
    print("{} {} {} = {}".format(number1,operation,number2,answer))

    wanna_continue = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if wanna_continue == "y":
      number1 = answer
    elif wanna_continue == "n":
      continuation = False
      clear()
      calculator()



calculator()
