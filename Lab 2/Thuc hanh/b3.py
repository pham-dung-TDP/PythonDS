'''
Viết chương trình nhập vào thứ (1-7) trong tuần, nếu thứ không hợp lệ thì cho nhập lại.
Sau đó cho biết thứ đã nhập có tên là gì và xuất kết quả ra màn hình 
VD: (Nhập 1: Chủ nhật , 2: Thứ hai, ...)
'''
thu = int(input("Nhập thứ: "))
if thu == 1:
    print("1: Chủ nhật")
elif thu == 2:
    print("2: Thứ 2")
elif thu == 3:
    print("3: Thứ 3")
elif thu == 4:
    print("4: Thứ 4")
elif thu == 5:
    print("5: Thứ 5")
elif thu == 6:
    print("6: Thứ 6")
elif thu == 7:
    print("7: Thứ 7")
else:
    print(f"Không có thứ: ",thu)