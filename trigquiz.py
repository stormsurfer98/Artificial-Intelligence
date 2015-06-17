from math import sqrt, sin, cos, tan, asin, acos, atan, atan2, degrees, radians, pi
x = (1+sqrt(5))/2
y = (x-1)/(x*x-x+1)
z = y - cos(radians(72))
print('1:', round(z, 3))
w = round(degrees(atan(sqrt(3))), 3)
print('2:', round(w, 3))
theta = atan(4/3); phi = atan(3/4)
print('3:', round(phi, 2))
print('4:', round(sin(theta) - cos(phi), 3))
print('5:', round(sin(theta+phi)+cos(radians(w)), 1))