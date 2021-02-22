x = "phan thanh chi"
y = 'chi' in x
print(y)
print("do dai chuoi",len(x) -1 )

a =10
b =30
c = a+ b
print('Tong cua no la %d + và %d la %d '  %(a,b,c))

s = f" {a:} {b:} {c}"
print (s)
s1 = 'toi yeu'
s2 = 'lap trinh'
print('{} khong the {}'.format(s1,s2))


# Định dạng chuỗi
#chuoi

#print('Die vao a = {} dien vao b={}'.format(1,2))

print('{: <30}'.format('phan thanh chi'))
print('{: >40}'.format('phan thanh chi'))
print('{: ^50}'.format('phan thanh chi'))