def calc(temp):
    for i in wind:
        chill = (35.74 + 0.6215*temp - 35.75*(i**0.16) + 0.4275*temp*(i**0.16))
        print(f"At temperature {temp}{unit}, and wind speed {i} mph, the windchill is: {chill:.2f}{unit}")
def calc(tempc):
    for i in wind:
        chill = (35.74 + 0.6215*tempc - 35.75*(i**0.16) + 0.4275*tempc*(i**0.16))
        chillc = ((chill - 32) * 5/9)
        print(f"At temperature {temp}{unit}, and wind speed {i} mph, the windchill is: {chillc:.2f}{unit}")
temp = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").upper()
chill = 0
wind = [5,10,15,20,25,30,35,40,45,50,55,60]
if unit == "C":
    tempc = (temp * 9/5) + 32
    calc(tempc)
if unit == "F":
    calc(temp)