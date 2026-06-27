with open('livros.txt', 'r', encoding= 'utf-8') as arquivos:
    lista=[]
    for linha in arquivos:
        dados = linha.strip().split(',')
        lista.append(dados)

print(len(lista))

