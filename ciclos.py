import time

#Opcion 1

lista = [] 
numero = 2
while numero <=500: 
    lista.append(numero)
    numero += 1
print(lista)



multiplo = 2
while multiplo <= 25:
    print("Multiplo de: ", multiplo)
    time.sleep(0.0000001)
    contador = 1
    while contador < len(lista):
        if(lista[contador] % multiplo == 0 ):
            print("Quitando: ",lista[contador])
            lista.remove(lista[contador])
            time.sleep(0.00001)
        contador +=1
    multiplo += 1
print(lista)
print(len(lista))


#Opcion 2
lista_ciclo = list(range(2, 501))
lista_ciclo_2 = list(range(2, 26))
for j in lista_ciclo_2:
    for i in lista_ciclo:
        if i%j == 0 and i!=2:
            lista_ciclo.remove(i)
print(lista_ciclo)
print(len(lista_ciclo))

