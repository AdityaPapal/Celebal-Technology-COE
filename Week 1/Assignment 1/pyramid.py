def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print("  ", end="")
        for k in range(2 * i + 1):
            print(f"* ", end="")
        print()

n = int(input("Enter the row and columns to print pyramid: "))
pyramid(n)
