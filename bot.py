# Assigning variables :-)
print("Hi, I am Marvin, your personal bot.")
print("lets move on.")
user_name=input("what is your name? :")
print ("welcome " + user_name)
command =input ("Do you want to add or substract some numbers ?")



if command == "add" or "+":           #addition section
    print("lets add some numbers")
    input1 = input("number 1> ")      #asking user to input some numbers
    input2 = input("number 2> ")
    num1 = int(input1)
    num2 = int(input2)
    result = num1 + num2
    print(result)
    output = str(result)              #casting int to str
    print = (input1 + "+" + input2 + "=" + output)
elif command == "substract" or "-":   #substraction section
    print("lets substract some numbers")
    input1 = input("number 1> ")      #asking user to input some numbers
    input2 = input("number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = num1 - num2
    print(result)
    output = str(result)              #casting int to str
    print = (input1 + "-" + input2 + "=" + output)
elif command == "average":
    how_many = input("how many numbers>")
    how_many = int(how_many)
    total = 0
    for number_count in range(how_many):
        number = input("Enter number " + str(number_count)+ " >")
        total = total + int(number)
    result = total / how_many
print("The average = " + str(result)
else:
    print("sorry i dont understand this")

