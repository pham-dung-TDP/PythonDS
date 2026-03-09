'''
In các số lẻ nhỏ hơn số được nhập từ bàn phím
'''
n = int(input("Nhập n: "))
if n == 1: 
    print("Không có số lẻ nào nhỏ hơn n")
else:
    print("các số lẻ nhỏ hơn", n , "là: ")
    for i in range (1 , n+1 ,2):
        if i == n: break
        print (i , end=' ')