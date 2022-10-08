#Clase que define un coordenada en un expacio de dos dimensiones
class punto:
    def __init__(self,x , y , pfin:bool):
        self.x=x
        self.y=y
        self.pfin= pfin
#Algoritmo de alta eficiencia "EUCLIDES" para calcular el maximo común divisor
def mcd (m, n):
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    r0 = m
    r1 = n
    r = n
    i = 2
    while r != 0:
        q = r0 // r1
        x = (x1*q) + x0
        y = (y1*q) + y0
        r = pow(-1,i) * x * m + pow(-1,i+1)*y*n
        x0 = x1
        y0 = y1
        x1 = x
        y1 = y
        r0 = r1
        r1 = r
        i = i + 1
    x = pow(-1,i-2) * x0
    y = pow(-1,i-1) * y0
    r = (x*m) + (y*n)
    return x
#Suma de puntos en el espacio de curvas elipticas
def suma(P : punto , Q:punto, p , a):
    if P.x % p !=  Q.x % p :
        if P.pfin == 0:
            puntoRes= punto(Q.x ,Q.y , Q.pfin )
            return puntoRes
        elif Q.pfin == 0:
            puntoRes= punto(P.x , P.y ,P.pfin)
        else:
            #print("calculamos primer caso P+Q ")
            inverso = mcd(Q.x-P.x , primo)
            m = ((Q.y - P.y) * inverso) % p
            x3 = (pow(m,2) - (P.x + Q.x)) % p
            y3 = (m *(Q.x-x3)-Q.y) % p
            puntoRes=  punto(x3 ,y3 , 1)
            #print(puntoRes.x, " : ", puntoRes.y, " : ", puntoRes.pfin)
            return puntoRes
    elif P.x == Q.x:
        if P.y == Q.y:
            #print("calculamos el caso donde P+Q = 2p")
            inverso = mcd(2*P.y , p)
            m = ((3*pow(P.x,2) + a)* inverso)%p
            x3 = (pow(m,2) - 2*P.x)%p
            y3 = (m*(P.x - x3)-P.y)%p
            puntoRes =  punto(x3 ,y3 , 1)
            #print(puntoRes.x, " : ", puntoRes.y, " : ", puntoRes.pfin)
            return puntoRes
        elif P.y == - Q.y :
            #print("calculamos el caso donde P = -Q")
            puntoRes =  punto(0,0,0)
            #print(puntoRes.x , " : " , puntoRes.y , " : " , puntoRes.pfin )
            return puntoRes
#Multiplicación por escalares de puntos en espacio de curva eliptica
def lagrange(P: punto , n , primo , a ):
    if n == 0:
        sum = punto(0,0,0)
        return sum
    elif n >= 1:
        sum = punto(0,0,0)
        sumaux = punto(P.x,P.y,P.pfin)
        while n != 0:
            delta = n % 2
            if delta == 1:
                sum = suma(sum , sumaux ,primo, a)
            n = n >> 1
            sumaux = suma(sumaux, sumaux , primo , a)
        return sum
#Encriptación y desencriptación de mensaje
def ElGamal(primo , n, a ,b, a_llave , b_llave,G:punto, mensaje:punto):
    print(f"El mensaje original: ({mensaje.x},{mensaje.y},{mensaje.pfin})")
    A_publica = lagrange(G,a_llave,primo,a)
    print(f"La llave publica de a es: ({A_publica.x},{A_publica.y},{A_publica.pfin})")
    B_publica = lagrange(G,b_llave,primo,a)
    print(f"La llave publica de b es: ({B_publica.x},{B_publica.y},{B_publica.pfin})")
    #Encriptamos el mensaje
    Aux = lagrange(A_publica,b_llave,primo,a)
    mensajeEnc = suma(mensaje,Aux,primo,a)
    print(f"El mensaje encriptado es: ({mensajeEnc.x},{mensajeEnc.y},{mensajeEnc.pfin})")
    Aux2 = lagrange(B_publica , n -a_llave , primo ,a)
    mensajeDes = suma(mensajeEnc,Aux2,primo,a)
    print(f"El mensaje desencriptado es: ({mensajeDes.x},{mensajeDes.y},{mensajeDes.pfin})")
    if mensajeDes.x == mensaje.x:
        if mensajeDes.y == mensaje.y:
            if mensajeDes.pfin == mensaje.pfin:
                print("Concuerda con el mensaje original")

import time
def medirTiempo(primo , n, a ,b, a_llave , b_llave,G:punto, mensaje:punto):
    tiempo_inicial = time.time()
    ElGamal(primo ,n,a,b,a_llave,b_llave,G,mensaje)
    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("El tiempo de ejecución de esta iteración es:", tiempo_ejecucion)
    print("\n\n")



primo = 90252740485580524463
G = punto(11805259205692532806 , 46354324840815154177 ,1)
k = 90252740479876747494
a = 35
b = 34
a_llave = 921892889
b_llave = 2312312

mensaje = punto(55639260187278651316 , 14776186224911701337,1)
mensaje2 =  punto(77611194158697613036 , 69920476232577090712,1)
mensaje3 = punto(33436514455712827084 , 15294809265003198357 , 1)
mensaje4= punto(87926463288892695163 , 30605971112471359665 , 1)
mensaje5 = punto(85967798110992276241 , 12521236368971448935 , 1)
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje2))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje3))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje4))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje5))

primo = 98663929319600894747
G = punto(20788648160236000631 , 46583530757724383107 ,1)
k = 98663929312972804981
a = 59
b = 98
a_llave = 41747328
b_llave = 92873261
mensaje = punto(74844292949973389331 , 89007776809798364350 , 1)
mensaje2 =  punto(29161060318460036537 , 88097488526168293347,1)
mensaje3 = punto(48887416736145111639 , 53909911270572185647 , 1)
mensaje4= punto(3314012886009129628 , 6305181860754788579 , 1)
mensaje5 = punto(98520493672274892484 , 58022422649099021720 , 1)
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje2))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje3))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje4))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje5))


primo = 70345153933488770563254630892652791843098691555949
G = punto(69973922879588800865641931622085086204771500592822 , 35870564150676971517146082252955448314410468883126 ,1)
k = 70345153933488770563254631299203851571261753943248
a = 35
b = 90
a_llave = 417473283131231289
b_llave = 928732612131234435
mensaje = punto(28743068747961159712414415430015247052162032409951 , 5572335589947269320685861889932101687067846640722 , 1)
mensaje2 =  punto(62620554674158392129347638858298472786832971221418 , 34876453113989123193960802991749004005799822549908,1)
mensaje3 = punto(55710314773084435684047191133835471982252895809275 , 30647945097692833131559414313017353136805939871334, 1)
mensaje4= punto(57884298692217867662994891595425943051714716821387 , 13812815583384365346477507814935778788289805378217 , 1)
mensaje5 = punto(12128721325473813979662077660758872777931679472268 , 22940009016390159761481235084674014778861452518883 , 1)
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje2))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje3))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje4))
print(medirTiempo(primo, k, a, b, a_llave, b_llave, G, mensaje5))
