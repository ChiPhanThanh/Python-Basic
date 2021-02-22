file = open (" chi1 .txt ", "w")
a = []
N = int ( file . readline ())
for i in range (0,N):
 temp = int ( file . readline ())
 a. append ( temp )
 print (a)
file . close ()
