"""escribe un programa que muestre la sucesion fibonacci y que no supere al numero otorgado por
 el usuario """

n1=0
n2=1
n3=1
n4 = int (input("ingresa un numero: "))

print(n2)

for i in range(n4):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)

