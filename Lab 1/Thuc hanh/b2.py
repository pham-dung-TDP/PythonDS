'''Nhập giây từ bàn phím quy đổi sang ngày,giờ,phút,giây'''

s = int(input("Nhập giây: "))
ngay = s // 86400
s = s % 86400
gio = s // 3600
s = s % 3600
phut = s // 60
giay = s % 60
print("Ngày:", ngay, "Giờ:", gio, "Phút:", phut, "Giây:", giay)