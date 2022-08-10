#Program to Convert Weight of Kg's or Pounds to other
print ("\nHello, This Program is for Converting Weight Types")

#Allows input for an int only
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

#Ask User input for Weight
user_weight = get_int("Enter Weight to Convert: ")

#Ask User if they using Kgs or Pounds and print selected
unit_type = "0"
while True:
    if unit_type == "K":
        user_weight =  user_weight / .45
        print (f"Your Weight in Pounds is: {user_weight}")
        break
    elif unit_type == "L":
        user_weight = user_weight * .45
        print (f"Your Weight in Kg's is: {user_weight}")
        break
    else:
        unit_type = input("Is the weight in (K)g or (L)bs? ").upper()