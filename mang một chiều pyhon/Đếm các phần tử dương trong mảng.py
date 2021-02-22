# đếm các số lẻ ở trong mảng
a = []
cout = 0
n= int(input("Nhap số lượng phần tử mảng:="))
for i in range(0,n):
    temp = int(input("Xuất phần tư muốn nhập:=" + str(i)))
    a.append(temp)
    if( a[i] > 0):
        cout = cout + 1
print("\nXuất mảng vừa nhập", a)
print("\n\nSố lượng phần tử dương trong mảng một chiều là:=",cout)


a = []
n = int(input(" nhap vao n phan tử mảng:="))
cout = 0
for i in range(0,n):
    tem = int(input("mang la" + str(i +1)))
    a.append(tem)
    if( a[i] > 0):
        cout = cout + 1
print("Mang vua nhap la", a)
print("Số phần tử chẵn trong mảng là:=",cout)