# Escreva uma função chamada numeros_pares que receba uma lista de 
# números e retorne uma nova lista apenas com os números pares.

numeros = [1,2,3,4,5,6] #criando uma lista com todos os numeros
pares = [] # criando uma lista vazia

def numeros_pares(): #criando a função
    for numero in numeros: # loop for (vai itera sobre cada numero da lista)
        if numero % 2 == 0: # se o resto da divisão do numero por 2 for 0 (ele é par)
            pares.append(numero) # adiciona o numero na lista pares
    return pares # retorna a lista

resultado = numeros_pares() # adiciona a função em uma variavel
print("Numero pares:")
print(resultado) # retorna a variavel com a função
