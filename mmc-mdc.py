from math import prod

def numeros_do_intervalo(numero):
    numeros = []
    if(numero < 0):
        numero = numero * -1
    for i in range(2,numero + 1):
        if(numero%i == 0):
            numeros.append(i)

    return numeros        

def primo(numero):
    count = 0  
    if(numero < 0):
        numero = numero * -1
    for i in range(2,numero + 1):
        if(numero%i == 0):
            count += 1

    return count     

def expoente(array, numero):
    i = 0
    quociente_array = []
    count = 0
    original = numero

    while(i != len(array)):
        if(numero % array[i] == 0):
            quociente = numero / array[i]
            numero = quociente
            count += 1
        else:
            quociente_array.append(count)
            i += 1
            count = 0
            numero = original

    return quociente_array

def decompor(numero):
    array = numeros_do_intervalo(numero)
    fatoers_primos = []

    for item in range(0,len(array)):
        check = primo(array[item])
        if(check > 1):
            array[item] = 0
    
    for item in array:
        if(item != 0):
            fatoers_primos.append(item)  

    return fatoers_primos

def mdc(numero1, numero2):
    fatore1 = decompor(numero1)
    fatore2 = decompor(numero2) 
    fatore_aux = []

    expo1 = expoente(fatore1,numero1)
    expo2 = expoente(fatore2,numero2)
    expo_aux = []

    if(len(fatore1) >= len(fatore2)):
        for i in range(0,len(fatore1)):
            for j in range(0,len(fatore2)):      
                if(fatore1[i] == fatore2[j]):
                    fatore_aux.append(fatore1[i])

                    if(expo1[i] >= expo2[j]):
                        expo_aux.append(expo2[j])
                    else:
                        expo_aux.append(expo1[i])
    else:
        for i in range(0,len(fatore2)):
            for j in range(0,len(fatore1)):      
                if(fatore2[i] == fatore1[j]):
                    fatore_aux.append(fatore2[i])

                    if(expo2[i] >= expo1[j]):
                        expo_aux.append(expo1[j])
                    else:
                        expo_aux.append(expo2[i])
    
    result = []
    for i in range(len(expo_aux)):
        result.append(fatore_aux[i] ** expo_aux[i])
    print('')
    print("O MDC É",prod(result))

def remove_repetidos(lista):
    aux = []
    for i in lista:
        if i not in aux:
            aux.append(i)
    aux.sort()
    return aux

def mmc(numero1, numero2):
    fatore1 = decompor(numero1)
    fatore2 = decompor(numero2) 

    expo1 = expoente(fatore1,numero1)
    expo2 = expoente(fatore2,numero2)

    fatore_uni = fatore1 + fatore2
    fatores_comum = remove_repetidos(fatore_uni)
    expo_fatores_comum = []

    for i in range(0,len(fatores_comum)):
        for j in range(0,len(fatore1)):
            if(fatores_comum[i] == fatore1[j]):
                var1 = expo1[j]
                break
            else:
                var1 = 0

        for j in range(0,len(fatore2)):      
            if(fatores_comum[i] == fatore2[j]):
                var2 = expo2[j]
                break
            else:
                var2 = 0
                
        if(var1 >= var2):
            expo_fatores_comum.append(var1)
        else:
            expo_fatores_comum.append(var2)
                
    result = []
    for i in range(len(fatores_comum)):
        result.append(fatores_comum[i] ** expo_fatores_comum[i])
    print("O MMC É",prod(result))    

print("MDC E MMC")
numero1 = int(input("DIGITE UM NUMERO: "))
numero2 = int(input("DIGITE OUTRO NUMERO: "))

mdc(numero1, numero2)
mmc(numero1, numero2)
