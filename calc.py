def add(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
      return "Division by zero is not allowed"
    return x / y
def main():
    print("final output")

choice = input("This is for Addition '+'\nThis is for subtraction'-'\nThis is for Multiplacation'*'\nThis is for Division'/'\nEnter your choice ")
if choice in ['+','-','*','/']:
    try:
        num1 = float(input("enter first no."))
        num2 = float(input("enter second no."))
    except ValueError:
        print("invalid input . plese re-enter no.")
    if choice == '+':
        print(f"the result is:{add(num1 ,num2) }")
    elif choice =='-':
        print(f"the result is {subtract(num1,num2) }")
    elif choice =='*' :
        print(f" the result is {multiply(nmu,1, num2)}")
    elif choice =='/':
        print(f"the result is :{divide(num1, num2)}")

else:
    print(" Invalid input")  
if __name__=="__main__":
    main()