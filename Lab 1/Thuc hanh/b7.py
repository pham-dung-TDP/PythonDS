'''
Nhập tọa độ 3 đỉnh tam giác, xác định trọng tâm của tam giác đó
'''
x1,y1 = map(float,input("Nhập tọa độ 1: ").split())
x2,y2 = map(float,input("Nhập tọa độ 1: ").split())
x3,y3 = map(float,input("Nhập tọa độ 1: ").split())
x = (x1 + x2 + x3) / 3
y = (y1 + y2 + y3) / 3
print("trọng tâm của tam giác là: ", x , y)
