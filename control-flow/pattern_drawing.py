size = int(input("Enter the size of the pattern: "))
side = size
while size > 0:
    for i in range(1, side + 1):
        print("*", end="")
    print()
    size -= 1