print("Elige un número: tijera = 1 , piedra = 2 , papel = 3 , lagartija = 4 o spock = 5")
s1 = int(input())
s2 = int(input())

if s1 == 1:
    if s2 == 1:
        print("Empate")
    elif s2==2:
        print("Gana piedra")
    elif s2==3:
        print("Gana tijera")
    elif s2==4:
        print("Gana tijera")
    elif s2==5:
        print("Gana spock")
    else:
        print("Número inválido")
elif s1==2:
    if s2==1:
        print("Gana piedra")
    elif s2==2:
        print("Empate")
    elif s2==3:
        print("Gana papel")
    elif s2==4:
        print("Gana lagartija")
    elif s2==5:
        print("Gana spock")
    else:
        print("Número inválido")
elif s1==3:
    if s2==1:
        print("Gana tijera")
    elif s2==2:
        print("Gana papel")
    elif s2==3:
        print("Empate")
    elif s2==4:
        print("Gana lagartija")
    elif s2==5:
        print("Gana spock")
    else:
        print("Número inválido")
elif s1==4:
    if s2==1:
        print("Gana tijera")
    elif s2==2:
        print("Gana lagartija")
    elif s2==3:
        print("Gana lagartija")
    elif s2==4:
        print("Empate")
    elif s2==5:
        print("Gana spock")
    else:
        print("Número inválido")
elif s1==5:
    if s2==1:
        print("Gana tijera")
    elif s2==2:
        print("Gana piedra")
    elif s2==3:
        print("Gana spock")
    elif s2==4:
        print("Gana spock")
    elif s2==5:
        print("Empate")
    else:
        print("Número inválido")
