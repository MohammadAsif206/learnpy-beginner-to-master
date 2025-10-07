#Requirement is to print the menu, name of the food left aligned, proce right aligned, the space in the between should be
#filled with dashes. The total length of the print area is 20 spaces


check = True
dec = {}
while check:
    menuItem = input("Please enter the name of the food")
    price = input("Please enter the price")
    if len(menuItem)< 2:
        check = False
    else:
        totalLen = len(menuItem)+len(price)
        dashLen = 20- totalLen
        dash = "-"*dashLen
        print(f"{menuItem} {dash}${price}")



