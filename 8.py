#8.	Write a python program that asks the user to enter a length in centimeters. 
# If the user enters a negative length, the program should tell the user that the entry is invalid. 
# Otherwise, the program should convert the length to inches and print out the result. (2.54 cm=1 inch).

length_cm = float(input("Enter length in centimeters: "))
if(length_cm < 0):
    print("Invalid entry. Length cannot be negative.") 
else:
    length_inch = length_cm / 2.54
    print(f"{length_cm} cm is equal to {length_inch} inches.")
