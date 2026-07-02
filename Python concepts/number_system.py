while True:
    print("1.Decimal to Hexa")
    print("2.Decimal to Octal")
    print("3.Decimal to Binary")
    print("4.Exit")
    ch = int(input("Enter choice: "))

    d_num = int(input("Enter decimal number: "))
    if ch == 1:
        print(f"{d_num} Hexa {hex(d_num)}")
    elif ch == 2:
        print(f"{d_num} Octal {oct(d_num)}")
    elif ch == 3:
        print(f"{d_num} Binary {bin(d_num)}")
    elif ch == 4:
        break
    else:
        print("Invalid choice")
