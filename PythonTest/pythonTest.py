# pythonTest.py

from add_fun import *
from mul_fun import *

Num1 = int(input("Enter number 1: "))
Num2 = int(input("Enter number 2: "))
Num3 = int(input("Enter number 3: "))

add_result = addNum(Num1, Num2, Num3)
Mul_result = mulNum(Num1, Num2, Num3)

print("Addition = ", add_result)
print("Multiplication = ", Mul_result)

