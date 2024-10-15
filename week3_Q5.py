# Write the algorithm for a program that sets the weight of a parcel to 12g. If the weight is 8 g or
# less, there is delivery charge of a flat fee of $1.50. If the weight is more than 8 g then $1.50 plus
# $0.50 for each gram over 8g is charged for delivery. The program displays the weight and the
# delivery fee. Use both pseudocode and a flowchart.


parcel_weight = float(input("How many grams does the parcel weigh: "))

if parcel_weight <= 8:
    cost = float(1.50)
    
else:
    aditional_weight = parcel_weight - float(8.0)
    math = aditional_weight * 0.5
    cost = float(1.50 + float(math))
    print(str(aditional_weight) + " extra grams")

print(f"The weight of your parcel is {float(parcel_weight)} grams")
print(f"Total charge will be: ${cost}0 AUD")







    


