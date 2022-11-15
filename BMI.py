print("           BMI Calculator \n ==================================")
#Khalifa Khalid 7E1
n=input("number of users: ")
name=input("What is your name? ")
weight=float(input("Okay "+name+", what is your weight in kilograms? "))
height=float(input("And what is your height in meters? "))
BMI=weight/(height**2)

if BMI<=18.5:
    print("You are underweight, "+name+", you should eat more.")
if BMI>18.5 and BMI<25:
    print("Your weight is healthy, "+name+". Great!")
if BMI>=25 and BMI<30:
    print("You are overweight, "+name+", you should work out more.")
if BMI>=30:
    print("You are obese, "+name+", you should work out more and eat healthier food.")
BMI=round(BMI,1)
BMI=str(BMI)

print("your BMI is "+BMI)
input("press enter to quit")
