#Nhap vào amgnr của n và tinh tong

a = []
n = int(input(" Nhap vao so luong phan tu cho mảng a la:"))
tong =0
for i in range(n):
    temp = int ( input (" Nhap phan tu thu"+ str (i+1))) #khai bao 1 biến và i+1 chuyên về kiểu string
    a.append ( temp )
    tong = tong + a[i]
print(a)
print(" Tong cua mang la",tong)



