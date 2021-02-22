# tinh tong s = + 2 +3...n

def tong(n):
    if (n == 1):
          return 1
    else:
      return (n) + tong(n-1)
n=int(input("nhap vao n="))
print("Tong",tong(n))




