childmeal = input("Price of child's meal: ")
adultmeal = input("Price of adult's meal: ")
childnum = input("Number of children: ")
adultnum = input("Number of adults: ")
salestax = float(input("Sales tax rate: "))
float_childmeal = float(childmeal)
float_adultmeal = float(adultmeal)
int_childnum = int(childnum)
int_adultnum = int(adultnum)
float_salestax = float(salestax)
subtotal = float_childmeal * int_childnum + float_adultmeal * int_adultnum
print(f"Subtotal: ${subtotal}" )
salestaxtotal = (salestax/100) * subtotal
salestaxtotal1 = round(salestaxtotal, 2)
print(f"Sales Tax: ${salestaxtotal1}")
total = subtotal + salestaxtotal
print(f"Total: ${total}")
payment = float(input("What is the payment amount? "))
change = payment - total
change1 = round(change, 2)
print (f"Change: ${change1}")