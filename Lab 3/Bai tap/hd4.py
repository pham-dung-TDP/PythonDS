'''
Tính giai thừa n được nhập từ bàn phím
'''
n = int(input("Nhập n: "))
tich = 1
for i in range (1, n+1):
    tich *= i
print(n,"!= ", tich)