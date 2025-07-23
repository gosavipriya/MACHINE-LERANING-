
print("Hello T3")


a =10
b =5
print("Add:", a + b)
print("Sub:", a - b)
print("Multip", a * b)
print("Div", a / b)




def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Multip")
    print("4. Div")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid Input")

calculator()



import matplotlib.pyplot as plt

x =[2,4,6]
y =[1,3,5]

plt.xlabel("x Axis")
plt.ylabel("y Axis")
plt.show()