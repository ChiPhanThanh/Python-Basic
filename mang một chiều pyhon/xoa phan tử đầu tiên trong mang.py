# Ta duyert tu trai qua phai. Xuat phat từ vị trí càn xóa dời phần tử vè phía trước
#cho đến khi kết thúc mảng sau đó giảm kích thước mảng


a = []
n = int(input(" Nhập vao n="))
for i in range(n):
    temp = int(input("mảng phần tử:" + str(i+1)))
    a.append(temp)
print("\n\t\tMang vừa nhạp là:=",a)

for i  in range(n-1):
    a[i] = a[i+1]
print("mang da xoa phan tu dau la",a)

