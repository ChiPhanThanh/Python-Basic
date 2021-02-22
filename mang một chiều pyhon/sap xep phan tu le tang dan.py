#sap xep cac phan tu le tang dant

def xeple(a,n):
    for i in range(n):
        for j in range(n):
            if((a[i]< a[j]) and (a[i]%2 != 0) and (a[j] % 2 != 0)):
                tempt = a[i]
                a[i] = a[j]
                a[j] = temp
            
a = []
n = int(input(" Nhap vao n="))
for i in range(n):
    temp = int(input("xuat mang"+ str(i)))
    a.append(temp)
print("Xuất mảng", a)
print("xuat",xeple(a,n))


