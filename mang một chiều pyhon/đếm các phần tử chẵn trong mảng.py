#nhap vao một mảng và đếm các phần tử trong mảng

a = []
n = int(input(" nhap vao n phan tử mảng:="))
cout = 0
for i in range(0,n):
    tem = int(input("mang la" + str(i +1)))
    a.append(tem)
    if( a[i] %2 == 0):
        cout = cout + 1
print("Mang vua nhap la", a)
print("Số phần tử chẵn trong mảng là:=",cout)


