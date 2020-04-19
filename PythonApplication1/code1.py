from math import sin, cos, radians
# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    return ' ' * int(20 * cos(radians(x)) + 20) + 'o'

#print(make_dot_string(90))
#print(make_dot_string(180))
#print(make_dot_string(135))

##for i in range(360):
#for i in range(1):
#    s = make_dot_string(i)
#    print(s)

#cosine wave
#for i in range(0, 360, 12):
for i in range(0, 1800, 12):
    s = make_dot_string(i)
    print(s)