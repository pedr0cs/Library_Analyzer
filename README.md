# Library Analyzer
Script em Python que lê um arquivo de texto contendo dados de livros e gera estatísticas automáticas sobre uma biblioteca pessoal.

## Objetivo
Praticar manipulação de arquivos, estruturas de dados e lógica de programação em Python, construindo uma ferramenta simples e útil: um analisador de biblioteca que processa dados de livros e responde perguntas como "qual autor eu mais leio?" ou "qual gênero é mais comum na minha lista?".

## Tecnologias
- Python 3

## Funcionalidades
- [x] Leitura de arquivo `.txt` com dados de livros
- [x] Processamento e organização dos dados em dicionários
- [x] Função para extrair valores únicos (autores, títulos, gêneros sem repetição)
- [x] Tratamento de erros para linhas mal formatadas (com identificação da linha problemática)
- [x] Estatísticas: total de livros, autor mais frequente, gênero mais lido

## Como rodar
```bash
python livro.py
```

## Exemplo de saída
O total de livros são: 14
O autor mais frequente é: Rebecca Yarros
O gênero mais lido foi: Fantasia / Romance

## Dificuldades reais que tive
Documentando aqui porque acho que mostra mais que só o código funcionando:

- Fiquei um tempo travado porque usei o mesmo nome pra duas variáveis diferentes dentro de um `for`, e isso fazia minha lista "desaparecer".
- Não entendia por que o `.strip()` não tirava um espaço que estava sobrando no meio da linha. Descobri que ele só limpa as pontas (início e fim), então precisei usar ele de novo depois de separar os dados.
- Demorei bastante pra entender como funciona uma função com dois parâmetros, onde um é a lista toda e o outro é só o nome do dado que eu quero pegar dela.
- Tive meu primeiro conflito de Git, depois de editar um arquivo direto no site do GitHub sem sincronizar com meu computador antes. Aprendi a sempre puxar (`pull`) antes de mexer em lugares diferentes.
- Cheguei a tentar fazer o código tratar empate (dois autores com mesmo número de livros), mas vi que ia complicar demais pra algo que não era essencial agora. Preferi simplificar e seguir.

## 📌 Status
✅ Projeto concluído — parte de uma série semanal de estudo em Python.