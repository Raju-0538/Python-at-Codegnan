# importing the file
import addition

# importing function from module
from  subtraction import sub

# importing module with alias name
import multiplication as mul

# import function with alias name
from division import div as divi

from sqrt import sq_root
from square import square
from modulo import modulo
from floor import floor

print(addition.add(3,5))
print(sub(10,3))
print(mul.mul(2,10))
print(divi(20,4))
print(sq_root(9))
print(square(3))
print(modulo(10,3))
print(floor(10,3))