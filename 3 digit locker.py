def generate_password(arr, current):
    if len(arr) == len(current):
        print(current)
        return
    for digit in arr:
        if digit not in current:
            generate_password(arr, current=current + digit)


digit = ["1", "2", "3"]
generate_password(digit, "")