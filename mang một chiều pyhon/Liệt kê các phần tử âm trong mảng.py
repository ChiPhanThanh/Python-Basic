#Đếm các phần tử âm trong mảng
a = []
n =int(input(" nhap vao n="))
cout = 0
for i in range(0,n):
    temp = int(input("nhap phần tử vào mảng=" + str(i+1)))
    a.append(temp)
    if(a[i] < 0):
        cout = cout +1
print("Xuất mảng vừa nhập",a)
print(" Số lượng phần tử âm ở trong mảng là %d",cout)


