"""
Extra ->  https://www.youtube.com/watch?v=0_dQpUtcubM&ab_channel=GvahimClass difference between IS and == 
"""
if __name__ == '__main__':

    check = 21
    if check == 21:
        print("Hello 1 ")
        print(f"Hello, my number is {check}")

    check_2 = 23
    if check + check_2 is 44:  # here we should use == because of equality, its better practice.!
        print("Sum is 44")

    if check + check_2 == 44:
        print("Sum is 44")

    if check > 10:
        if check > 25:
            print("Bigger than 25")
        elif check > 20:
            print("Bigger than 20")
    else:
        print("Less than 10")

    if check == 21 and check_2 == 23:
        print(f"{check}, {check_2}")
