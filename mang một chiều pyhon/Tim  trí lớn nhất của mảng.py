def timkiem(a,n):
    for i in range(n):
        max = a[0]
        tem = 0
    if(a[i] < max ):
        max = a[i]
        tem = i #biến chỉ số
    return i+1


a = []
n = int(input(" Nhap vao n="))
for i in range(n):
    temp = int(input("xuat mang"+ str(i)))
    a.append(temp)
print("Xuất mảng", a)
print("Phần tử lớn nhất nhất trong mảng=", timkiem(a,n))

