a = int(input('nhap vao canh a='))
b = int(input('nhap vao canh b='))
c = int(input('nhap vao canh c='))

# tim dieu kien de thanh lam ba canh tam giac
if(( a == b) & (b == c) & (c ==a) ):
    print(" Ban vua nhap là Tam Giac Đều")
elif(( a ==b) or (b ==c) or  (c == a)):
    print(" Đó la tam giac can")
elif(( a*a ==b*b + c*c ) or (c*c == b*b + a*a) or ( b*b == a*a + c*c)):
    print(" Đo la tam giac vuong")
else: 
    print(" Cac canh ban vua nhap Khong phai tam giac")


