# the floor and ceil functions are in the math module
import math

# ceil returns the closest integer greater than or equal to the number
# (so it always rounds up)
i = math.ceil(5.834)

print(i)

# floor returns the closest integer less than or equal to the number
# (so it always rounds down)
i = math.floor(5.834)

print(i)

# round returns the closest integer to the number
# (so it rounds up or down)
# Note that this is a built-in function -- we don't need to import math to use it.
i = round(5.834)

print(i)