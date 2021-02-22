#Nhap vao ba so a, b, c
a = int(input(" Nhap vao gia tri a="));
b = int(input(" nhap vao gia trị b ="));
c = int(input(" nhap vao gia trị c ="));

if a <= b <= c:
    print("%d %d %d" % (a, b, c))
elif a <= c <= b:
    print("%d %d %d" % (a, c, b))
elif b <= a <= c:
    print("%d %d %d" % (b, a, c))
elif b <= c <= a:
    print("%d %d %d" % (b, c, a))
elif c <= a <= b:
    print("%d %d %d" % (c, a, b))
else:  # c <= b <= a
    print("%d %d %d" % (c, b, a))

