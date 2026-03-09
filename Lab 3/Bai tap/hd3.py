'''
Tính tổng các số chia hết hết cho 3 nhưng không chia hết cho 5 trong [1000-3000]
'''
tong = 0
for i in range (1000, 3000):
    if i % 3 == 0 and i % 5 != 0:
        tong += i
print ("Tổng các số chia hết cho 3 và ko chia hết cho  5 là: ", tong)       
