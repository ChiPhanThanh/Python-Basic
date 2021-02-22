def tong(a,b):
    return a+b
print('tong',tong(5,7))

def tong(a,b):
    return a*b
print('tong',tong(5,7))

def tong(a,b):
    return a-b
print('tong',tong(5,7))






def phep(a):
    print('in ra a',a)
phep(7)


def tong(text,age):
    print(text)
    print(age)
tong("chap phan thnah chi",69)

#ham không có tham số và không có gia trị trả về
def chao():
    print("chao phan thanh chi")
chao()


chao()#ham có tham số nhưng không có giá trị trả về
def ten(ho):
     #than hàm
     print("Hello"," " + ho.title())
name  = "chi"
ten(name)

#ham vs nhieu tham so
def tong1(a,b,c):
    print("Tong la", a+b+c)
a  = 10
b = 20
c = 40
tong1(a,b,c)

#ha, v s nhieu tham so có the thay đoi đk
def tong2(a,b,c):
    print(a+c+b)
a,b,c =  10,60,23
tong2(a,b,c)

def tong3(*a):
    tong = 0;
    for i in a:
        tong = tong + i
    print("phep tong cua no la",tong)
x1, x2,x3 = 10, 5,4
tong3(x1,x2,x3)

#hàm với tham số mặc định
def nhan( a, b= 23):
    print("phep nhan",a*b)
a = 3
nhan(a) 


#
def tentuoi(ten,tuoi ='29'):
    print(" ho ten cua toi:" + ten.title());
    print("tuoi cua toi:" + tuoi)
name = 'chi'
tentuoi(name)

#Ham co gai tri tra ve : 
def tinhtong(n,m):
    return n+m


# Ham có nhiều tham số













