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
        
    expo = expoente(fatoers_primos,numero)
    for i in range(0,len(fatoers_primos)):
        print (fatoers_primos[i], "^", expo[i])


print("LISTA DE FATORES PRIMOS")
numero = int(input("DIGITE UM NUMERO: "))
if(numero == 1):
    print([1])
else:
    decompor(numero)