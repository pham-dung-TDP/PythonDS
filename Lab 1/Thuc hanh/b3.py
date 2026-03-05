'''Nhập x. Tính:
f(x)= (-x + (căn bậc 2 của (x^2) + 4) )/ (căn bậc 7 của (x^4) + 1)
'''
import math
x = float(input("Nhập x: "))
f = (-x + math.sqrt(x*x + 4)) / ((x**4 + 1) ** 1/7)
print("Giá trị cùa f(x) là: %0.2f'" %f)