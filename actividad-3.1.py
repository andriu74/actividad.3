def S(a,b):
    return a+b
def R(a,b):
    return a-b 
def M(a,b):
    return a*b
def D(a,b):
    return a/b    
c=True
while True:
    print("la opcion 1 para suma")
    print("la opcion 2 para resta")
    print("la opcion 3 para multiplicacion")
    print("la opcion 4 para divicion")
    print("la opcion 5 para salir")
    c=input("dijite la opsion:  ")
    if c=="1":
        n1=float(input("dijite un mumero:  "))
        n2=float(input("dijite un mumero:  ")) 
        print("la suma es: ",S(n1 , n2))
    elif c=="5":
        break
    elif c=="2":
        n1=float(input("dijite un mumero:  "))
        n2=float(input("dijite un mumero:  "))
        print("la Resta es: ",R(n1 , n2))
    elif c=="3":
        n1=float(input("dijite un mumero:  "))
        n2=float(input("dijite un mumero:  "))
        print("la Multiplicacion  es: ",M(n1 , n2))
    elif c=="4":
        n1=float(input("dijite un mumero:  "))
        n2=float(input("dijite un mumero:  "))
        print("la Multiplicacion  es: ",D(n1 , n2))
    else:
        print("la opcion que dijito no se encuentra")