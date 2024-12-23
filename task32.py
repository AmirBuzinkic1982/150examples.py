import math

radius=int(input("Enter the radius:  "))
depth=int(input("Enter the depth:  "))
circle_area=math.pi*(radius**2)
total_volume=circle_area*depth
print(round(total_volume,3))