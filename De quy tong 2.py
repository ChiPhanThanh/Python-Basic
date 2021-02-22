
#s = 1 + 3 + 5....n
def tong(n):
  

    if(n==1):
      return 1
    else:
      return n + tong(n-2 )
n=int(input("nhap vao n="))
print("Tong",tong(n))


#tinh tong phan so: s = 1/1 + 1/2+ 1/3

def tongphanso(n1):
    if( n1 == 1): return 1
    else:
        return 1/n1 + tongphanso(n1 - 1)
n1 = int(input("Nhap vao n1=" ))
print("Tong phan so bạn vua nhap la", tongphanso(n1))

#tinh tong phan so: s = 1/2 + 1/4+ 1/6....1/n
def tongphanso(n2):
    if( n2 == 2): return 0.5
    else:
        return 1/n2 + tongphanso(n2 - 2)
n2 = int(input("Nhap vao n1=" ))
print("Tong phan so bạn vua nhap la", tongphanso(n2))

# Tính tong s = 1^2 + 2^2+ 3^3....n^2 - xem lại 
def tong3(m):
    if( m == 1 ): return 1
    else:
        return ( 1/tong3(n-1) + n*n) + tong3(n-1)
m = int(input("nhap vao m"))
print("ket qua", tong3(m))