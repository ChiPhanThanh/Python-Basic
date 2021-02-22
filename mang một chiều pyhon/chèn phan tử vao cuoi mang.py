a = []
n = int(input("Nhap vao n="))
for i in range(n):
    temp = int(input("xuat mang"  + str(i)))
    a.append(temp)
print("Xuat mảng vừa nhập",a)


def chen(x,n,a):
    for i in range(n-1):
        a[n]= x
x = int(input("Nhap vao x="))
chen(x,n,a)