weight = float( input("What is your weight?: ") )
height = float( input("What is your height?: ") )

bmi = (weight / height**2)

if(bmi <= 18.5):
    print("underweight")
elif(bmi > 18.5 and bmi <= 24.9):
    print("normal weight")
elif(bmi > 30):
    print("obesity")
    
