with open('livros.txt', 'r', encoding= 'utf-8') as arquivos:
    lista=[]
    for linha in arquivos:
        dados = linha.strip().split(',')
        dicionario = {
    'titulo': dados[0].strip(), 'autor': dados[1].strip(), 'paginas': dados[2].strip(), 'genero': dados[3].strip()
        }
        lista.append(dicionario)
              
def repeticoes(livros, informacao):
    lista_limpa= []
    for dicionario in livros:
        lista_limpa.append(dicionario[informacao])
    return list(set(lista_limpa))

titulos_unicos = repeticoes(lista, 'titulo')
autores_unicos = repeticoes(lista, 'autor')
generos_unicos = repeticoes(lista, 'genero')

for autor in autores_unicos:
    print(autor)