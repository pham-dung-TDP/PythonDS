print("-----Menu-----")
print("1.Coffe")
print("2.Cam vắt")
print("3.Nước ép cà rốt")
print("4.Nước lọc")
print("5.Nước dừa")
print("0.Không chọn gì nữa \n")
n = int(input())
while 0 <= n <= 5:
    n = int(input("Mời quý khách chọn đồ: "))
    if n == 1:
        print("Coffe")
    elif n == 2:
        print("Cam vắt")
    elif n == 3:
        print("Nước ép cam")
    elif n == 4:
        print("Nước lọc")
    elif n == 5:
        print ("Nước dừa")
    else:
        print ("Thôi")
        break