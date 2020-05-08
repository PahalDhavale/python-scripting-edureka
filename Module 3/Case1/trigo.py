#Write a program to find distance between two locations when their latitude and longitudes are given.
import math
from math import cos,sin,tan,atan,sqrt

Lon1= float(input("Enter Longitude of Place A"))
Lat1=float(input("Enter Latitude of Place A"))
Lon2=float(input("Enter Longitude of Place B"))
Lat2=float(input("Enter latitude of Place B"))
#Haversine
#formula:	a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
#c = 2 ⋅ atan2( √a, √(1−a) )
#d = R ⋅ c
#where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);


#Converting in radians

Lon1_rad=math.radians(Lon1)
Lat1_rad=math.radians(Lat1)
Lon2_rad=math.radians(Lon2)
Lat2_rad=math.radians(Lat2)

LT=Lat2_rad-Lat1_rad
LO=Lon2_rad-Lon1_rad
R=6371

a = ((sin(LT/2)**2) + cos(Lat1_rad) * math.cos(Lat2_rad)* (math.sin(LO/2)**2))

c= 2* math.atan2(math.sqrt(a) , math.sqrt(1-a))

d= R * c
print(d)
