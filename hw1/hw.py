a = int(input(" Введите a "))
b = int(input("Введите b "))
c = int(input('Введите c '))
z = a*c
if z + b == 0:
    print("c является решением линейного уравнения ax + b = 0")
else:
    print("c не является решением линейного уравнения ax + b = 0")



if a == 0 or b == 0:
    print ('a не даёт остаток c при делении на b')
else:
    q = a % b 
    if q - c == 0:
        print("a даёт остаток c при делении на b")
    else:
        print("a не даёт остаток c при делении на b")
 
