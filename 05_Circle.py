import math

radius = float (input("Please provide with a radius of circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("Area of your circle is: ", round(area,2))
print("Circumference of your circle is: ", round(circumference,2))
