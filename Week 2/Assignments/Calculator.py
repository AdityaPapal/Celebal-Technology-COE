ans = 0

while(True):
    ch = input("Enter the Operator (for exit enter 'x': ")
    if(ch == '+' or ch == '-' or ch == '*'  or ch == '/' or ch == '%'):
        num1 = int(input("Enter the first number:  "))
        num2 = int(input('Enter the Second nunmber: '))

        if(ch == '+'):
            sum = num1+num2
            print(f"Sum of {num1} & {num2}: {sum}")
            ans += sum

        if (ch == '-'):
            sub = num1 + num2
            print(f"Subtraction of {num1} &  {num2}: {sub}")
            ans += sub

        if (ch == '*'):
            mul = num1 + num2
            print(f"Multiplication of {num1} &  {num2}: {mul}")
            ans += mul

        if (ch == '/'):
            division = num1 + num2
            print(f"Division of {num1} &  {num2}: {division}")
            ans += division

        if (ch == '%'):
            mod = num1 + num2
            print(f"Division of {num1} &  {num2}: {mod}")
            ans += mod
        print(f"Total ans is {ans} ")
    elif ch == 'X' or ch =='x':
        break
    else:
        print("Invalid Operator")

print()
print(f"The total calculated answer is {ans}")