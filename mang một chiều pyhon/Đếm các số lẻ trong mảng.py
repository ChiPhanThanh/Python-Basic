# đếm các số lẻ ở trong mảng
a = []
cout = 0
n= int(input("Nhap số lượng phần tử mảng:="))
for i in range(0,n):
    temp = int(input("Xuất phần tư muốn nhập:=" + str(i)))
    a.append(temp)
    if( a[i] % 2 != 0):
        cout = cout + 1
print("Xuất mảng vừa nhập", a)
print("Số lượng phần tử lẻ trong mảng một chiều là:=",cout)

