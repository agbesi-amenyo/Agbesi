weight = input("Weight: ")
unit  = input ('(L) lb or (K)g: ')
if unit.upper() == "K":
    converted = int(weight) / 0.45
    print(f'You are {converted} pounds ')
elif unit.upper() == "L":
    converted= int(weight) * 0.45
    print(f"Your weight is {converted} kilos")
else :
    print("Please enter valid unit. Thank you !")
