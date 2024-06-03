n = int(input("Enter the number of Row's and Column: "))

def lower_triangle(n):
    for i in range(0,n+1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

lower_triangle(n)
