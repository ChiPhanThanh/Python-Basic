#n! = 1.2.3.4.5....n
def giaithua(n):
    if (n == 0):
        return 1
    else:
        return n*giaithua(n - 1)
so =int(input("nhap vao n="))
print(" Tong cua n!=",giaithua(so))

#Dequy tinh tong s = 1 + 2 + 3 + 4....n

 
