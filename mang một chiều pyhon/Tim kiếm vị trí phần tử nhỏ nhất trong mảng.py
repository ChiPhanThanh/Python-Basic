def timkiem(a,n):
     for i in range(n):
                min = a[0]
                tem = 0
     if(a[i] > min ):
                min = a[i]
                tem = i
     return tem +1

a = []
n = int(input(" Nhap vao n="))

for i in range(n+1):
    temp = int(input("xuat mang" + str(i)))
    a.append(temp)
print("Xuất mảng", a)
print("Phần tử nhỏ nhất trong mảng=", timkiem(a,n))

