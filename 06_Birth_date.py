birthdate = input("Please provide your birth date in format DD-MM-YYYY: ")
months = ("January", "February","March","April","May","June","July")
month = int(birthdate[3:5])
print("You were born in " , months[int(birthdate[3:5])-1])
