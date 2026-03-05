'''
Nhập a, b, c  của 1 ptrinh b2: ax^2 + bx + c = 0
Tìm nghiệm của ptrinh đó
'''
import math
a , b , c = map(int,input ("Nhập 3 số: ").split())
delta = b*b - 4*a*c 
if delta > 0 :
    n1 = (-b + math.sqrt(delta) )/ 2*a
    n2 = (-b - math.sqrt(delta) )/ 2*a
    print("Nghiệm của ptrinh là x1: ", n1 , "x2: ", n2 )
else:
    print("Phương trình vô nghiệm")
