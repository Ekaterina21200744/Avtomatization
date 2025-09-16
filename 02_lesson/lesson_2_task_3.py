import math
def square (side):
    result = side*side
    return math.ceil(result)

side = int(input ("Сторона:"))   
result = square (side)
print(result)
