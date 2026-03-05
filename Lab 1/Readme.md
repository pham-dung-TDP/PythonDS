# Nhập xuất dữ liệu cơ bản 
## 1.1: Khái niệm biến nhớ
- Biến nhớ gọi tắt là biến
- Biến trong Python không cần khai báo trước (không cần khai báo kiểu dữ liệu)
- Khi ta gán giá trị cho biến thì nó sẽ tự động định dạng kiểu dữ liệu cho biến
## 1.2: Kiểu dữ liệu
- Một số kiểu dữ liệu phổ biến trong Py: int(số nguyên), float(số thực), bool(True/False), str(Chuỗi kí tự), ...
- VD: ``` a = 5 ```  ( a là tên biến , 5 là giá trị gán cho biến , kiểu dữ liệu int)
- VD: ``` a = "xin chào" ```  (a là tên biến, xin chào là kiểu dữ liệu chuỗi kí tự) ....
## 1.3: Các hàm nhập xuất dữ liệu trong python: 
### Hàm nhập dữ liệu từ bàn phím
- input() được dùng để nhập từ bàn phím. Kiểu dữ liệu của nó mặc định là chuỗi kí tự
- VD: ``` input("") ``` bên trong dấu nháy là chuỗi kí tự mà người dùng muốn nhập
- VD: ``` a = int(input("")) ``` do mình gán cho a là kiểu dữ liệu số nguyên. Nên người dùng nhập từ bàn phím bắt buộc phải là 1 số nguyên.
### Hàm xuất dữ liệu print()
- Hàm ``` print() ``` trong py là để in ra màn hình để hiện thị (không có chức năng nhập từ bàn phím)
- Cú pháp đầy đủ: ``` print(*object , sep= '' , end='') ```
- ' * ' : là có thể truyền nhiều giá trị nhưng mà phải ngăn cách nhau bằng dấu , 
- 'object' : là dữ liệu in ra màn hình
- VD: ``` print("a" , "b" ) ``` khi in ra màn hình nó sẽ hiện thị: a b
- 'sep' : là ký tự ngăn cách giữa các giá trị
- VD: ``` print("A", "B", "C", sep='-') ``` khi in ra màn hình nó sẽ hiển thị: A-B-C . Nếu như mà không truyền gì vào bên trong sep thì nó sẽ viết liền nhau
- 'end' : là ký tự được in ở cuối dòng 
- VD: ``` print("Hello", end=' \n') ``` khi in ra màn hình nó sẽ tự động xuống dòng. Nếu không truyền gì vào trong end thì nó cũng sẽ viết liền nhau
- VD: 
``` bash
    print("Hello", end='')
    print("World")
``` 
nó sẽ in ra HelloWorld
- Trong thực tế thì không dùng nhiều như cú pháp đầy đủ của nó mà thường sử dụng cú pháp đơn giản
- VD: ```print ("Hello")``` khi hiển thị ra màn hình nó sẽ có chữ Hello