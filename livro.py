with open('livros.txt', 'r', encoding= 'utf-8') as arquivos:
    lista=[]
    for linha in arquivos:
        dados = linha.strip().split(',')
        lista.append(dados)


print(lista[0])
print(lista[0][0])
print(lista[0][1])
print(lista[0][2])
print(lista[0][3])
