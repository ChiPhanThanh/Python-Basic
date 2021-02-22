
#liệt kê các phần tử mảng bé hơn x trong mảng
def Dem(a,n,x):
    Dem = 0
    for i in range(n):
      if(a[i] < x): # kiểm tra điều kiện
         print("\ncác phần tử bé hơn",x,"=", a[i])
  
def Demam(a,n):
    Dem1 = 0
    for i in range(n):
      if(a[i] < 0): # kiểm tra điều kiện
         print("\ncác phần tử âm hơn","=", a[i]) 

def Demduong(a,n):
    Dem2 = 0
    for i in range(n):
      if(a[i] > 0): # kiểm tra điều kiện
         print("\ncác phần tử duong hơn","=", a[i])  
  

a  =[]
n =int(input("Nap vao phan tử n="))
for i in range(n):
    temp = int(input("mang nhap" + str(i)))
    a.append(temp)
print("xuat mảng ", a)
x = int(input(" Nhạp vào giá trị x = "))
print("============= Liệt Kê Các Số Bé Hơn X===============Yêu ============")
f = Dem(a,n,x)
print("============= Liệt Kế Các Phần Tử Âm================Yêu===========")
Demam(a,n)
print("============= Liệt Kế Các Phần Tử Dương==============Yêu=============")
Demduong(a,n)
#print("các phần tử bé hơn", x,"là:=",f)

