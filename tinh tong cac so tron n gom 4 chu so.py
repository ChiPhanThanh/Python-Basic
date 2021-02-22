def tong(n):
    tl = 0
    while(n>0):
        dv  = n % 10  #chia lay du sau do gan vao mot bien dv
        if(dv % 2 != 0 ):
            tl  = tl + dv
        n = n//10 #lay so tiep theo sau khi da thuc thi chia lay nguyen
    return tl

x = tong(1234)
print(x)

