tu = float(input("Nhập tử: "))
while True:
    mau = float(input("Nhập mẫu: "))
    if mau != 0:
        phan_so = tu/mau
        print("kết quả: ", phan_so)
        break
    else:
        print("Nhập lại: ")