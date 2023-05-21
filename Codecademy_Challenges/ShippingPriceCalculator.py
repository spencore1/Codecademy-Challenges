weight = int(input("What is the weight of your package? "))

#Ground Shipping

if weight <= 2.00:
    cost = weight * 1.50 + 20
elif weight > 2 or weight <= 6:
    cost = weight * 3 + 20
elif weight > 6 or weight <= 10:
    cost = weight * 4 + 20
elif weight > 10:
    cost = weight * 4.75 + 20

print("Ground Shipping:", cost)

#Premium shipping
#prem = premium

prem = 125
print("Premium Shipping: ", prem)

#Drone shipping 

if weight <= 2:
    cost2 = weight * 4.50 
elif weight > 2 or weight <= 6:
    cost2 = weight * 9.00
elif weight > 6 or weight <= 10:
    cost2 = weight * 12.00
elif weight > 10:
    cost2 = weight * 14.25

print("Drone shipping: ", cost2)

