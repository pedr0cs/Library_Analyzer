with open('livros.txt', 'r', encoding= 'utf-8') as arquivos:
    lista=[]
    for numero, linha in enumerate(arquivos):
        dados = linha.strip().split(',')
        try:
            dicionario = {
    'titulo': dados[0].strip(), 'autor': dados[1].strip(), 'paginas': dados[2].strip(), 'genero': dados[3].strip()
        }
        except:
            print(f'Erro no livro {numero + 1}')
            break
        lista.append(dicionario)

def com_rep(data, books):
    lista_rep= []
    for dicionario in data:
        lista_rep.append(dicionario[books])
    return (lista_rep)

autores_frequentes = com_rep(lista, 'autor')
generos_frequentes = com_rep(lista, 'genero')

def repeticoes(livros, informacao):
    lista_com_repeticao = com_rep(livros, informacao)
    return list(set(lista_com_repeticao))

try: 
    titulos_unicos = repeticoes(lista, 'titulo')
    autores_unicos = repeticoes(lista, 'autor')
    generos_unicos = repeticoes(lista, 'genero')

    for genero in generos_unicos:
       print(genero, generos_frequentes.count(genero))
    #for autor in autores_unicos:
    #    print(autor, autores_frequentes.count(autor))
    #for titulos in titulos_unicos:
    #    print(titulos)
except:
    print('Infelizmente ocorreu um erro. Tente novamente')
