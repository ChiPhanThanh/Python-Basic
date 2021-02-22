
def demam(a,n):
    for i in range(n):
        dem = 0
        if(a[i] < 0):
            dem = dem + 1
        return dem

def demduong(a,n):
    for i in range(n):
        dem = 0
        if(a[i] > 0):
            dem = dem + 1
        return dem

a = []
n = int(input("Nhap vao n="))
for i in range(n):
    temp = int(input("xuat mang"  + str(i)))
    a.append(temp)
print("Xuat mảng vừa nhập",a)
print("Số lượng phần tử âm trong mảng", demam(a,n))
print("Số lượng phần tử âm trong mảng", demduong(a,n)


