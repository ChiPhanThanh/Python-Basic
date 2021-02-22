def hoanvi(c,d):
    tam = c
    c = d
    d = tam

def xeptang(a,n):
    for i in range(n):
        for j in range(i):
            if( a[i] % 2 == 0):
              hoanvi(c[i],d[j])

a = []
n = int(input(" Nhập vào n phần tử mang"))
for i in range(n):
    temp  = int(input("mảng thu tu phan tu="+ str(i)))
    a.append(temp)
print("Xuat mảng",a)

