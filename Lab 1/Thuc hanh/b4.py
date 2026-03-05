'''
Nhập 2 vecto và tính tích vô hướng của 2 vecto đó
'''

a = list(map(int,input("Nhập vecto 1: ").split()))
b = list(map(int,input("Nhập vecto 2: ").split()))
tich = 0
for i in range(len(a)):
    tich += a[i] * b[i]
print("Tích vô hướng =", tich)