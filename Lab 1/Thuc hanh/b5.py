'''một bóng đèn khi được sử dụng với hiệu điện thế 220V
 có cường độ dòng điện chạy qua là 2,7A. 
 Viết chương trình nhập vào thời gian sử dụng bóng đèn được tính bằng giây. 
 Tính tiền điện phải trả với giá tiền điện 7000đ  / kWh'''


t = float(input("Nhập thời gian sử dụng (giây): "))
u = 220
i = 2.7
p = u * i / 1000
a = p * (t / 3600)
tien = a * 7000
print("Tiền điện phải trả là:", tien)