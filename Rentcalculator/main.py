## input we needed from the users
# total rent 
# total food ordered for snacking
#electricity units spends
# water bill
#charge per unit
# persons staying in the flat

##output
## total amount you need to pay
 
while True:
    rent = int(input("Enter your total flat/hostel rent =  "))
    food = int(input("Enter your total food expenses =  "))
    electricity_units = int(input("Enter your total electricity units spent = "))
    charge_per_unit = int(input("Enter your charge per unit = "))
    persons = int(input("Enter total persons staying in the flat/hostel = "))
    water_bill = int(input("Enter your total water bill = " )) 

    total_bill = electricity_units * charge_per_unit

    output = (rent + food + total_bill) / persons


    print("Each person has to pay = ", output)
    print("Thanks")