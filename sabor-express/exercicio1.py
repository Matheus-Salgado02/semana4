numeros=[1,2,3,4,5,6,8,9,10]
numeros_decrescente=[]
nomes=['Alberto','Joao','Maria']
ano=['2002','2024']
soma=0
lista_media=[5,10,15]

def listar(lista):
    for listas in lista:
        print(listas)

def soma_impar(lista):
    soma = 0 
    for numero in lista:  
        if numero % 2 != 0: 
            soma += numero  
    return soma 

def imprimir_decrescente(lista,lista_decrescente):
    while lista:
        maior=lista[0]
        for numero in lista:
            if numero>maior:
                maior = numero
        lista_decrescente.append(maior)
        lista.remove(maior)
    for numero in lista_decrescente:
        print(numero)
        

def tabuada():
    resultado=[]
    numero= int(input('Informe um número:'))
    for i in range(0,11):
        resultado.append(numero*i)
    for res in resultado:
        print(res)

def soma_lista(lista):
    soma = 0
    for numero in lista:
        try:
            soma+=int(numero)
        except ValueError:
            print(f"Erro: O valor '{numero}' não é um número e será ignorado.") 
    print(soma)

def media(lista_numero):
    for numero in lista_numero:
        try:
            media = sum(lista_numero)/len(lista_numero)

        except ZeroDivisionError:
            print('Lista vazia')
        print(media)


        


# listar(numeros)
# listar(nomes)
# listar(ano)
# resultado = soma_impar(numeros)
# print(resultado)
# imprimir_decrescente(numeros,numeros_decrescente)
#tabuada()
#soma_lista(numeros)

media(lista_media)