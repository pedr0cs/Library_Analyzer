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

except:
    print('Infelizmente ocorreu um erro. Tente novamente')

autor_mais_frequente = ''
maior_contagem = 0

for autor in autores_unicos:
    contagem_atual = autores_frequentes.count(autor)
    if contagem_atual > maior_contagem:
        maior_contagem = contagem_atual
        autor_mais_frequente = autor

genero_mais_frequente = ''
maior_contagem = 0

for genero in generos_unicos:
    contagem_atual = generos_frequentes.count(genero)
    if contagem_atual > maior_contagem:
        maior_contagem = contagem_atual
        genero_mais_frequente = genero

print(f"O total de livros são: {len(lista)}")
print(f"O autor mais frequente é: {autor_mais_frequente}")
print(f"Os autores lidos foram: {', '.join(autores_unicos)}")
print(f"Os títulos lidos são: {', '.join(titulos_unicos)}")
print(f"O gênero mais lido foi: {genero_mais_frequente}")
print(f"Os gêneros lidos foram: {', '.join(generos_unicos)}")