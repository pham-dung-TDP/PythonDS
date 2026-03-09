'''
Nhập số điện và tính tiền
số điện <= 100 thì giá 2k
100 < số điện <= 200 giá 2,5k
200 < số điện <= 300 giá 3k
> 300 thì giá 5k
'''
sd = int(input("Nhập số điện đã dùng: "))
if sd <= 100:
    tien = sd * 2000
    print("Tiền điện phải trả là: ",tien)
elif 100 < sd <= 200:
    tien = sd * 2500
    print("Tiền điện phải trả là: ",tien)
elif 200 < sd <= 300:
    tien = sd * 3000
    print("Tiền điện phải trả là: ",tien)
else: 
    tine = sd * 5000
    print("Tiền điện phải trả là: ",tien)