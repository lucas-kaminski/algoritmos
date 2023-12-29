# Algoritmos

Scripts desenvolvidos durante a leitura do livro '[Entendendo Algoritmos: Um Guia Ilustrado Para Programadores e Outros Curiosos](https://www.goodreads.com/book/show/22847284-entendendo-algoritmos)'. Estes códigos participaram do meu aprendizado em algoritmos, conforme explorava o material e os conceitos apresentados.

# 1. Introdução a algoritmos

## Pesquisa linear

- A entrada pode ser qualquer lista.
- Percorre a lista do início ao fim, comparando cada elemento com o valor procurado.
- `O(n)`

## Pesquisa binária

- A entrada tem de ser uma lista ordenada.
- A cada passo, a lista é dividida pela metade e o elemento do meio é comparado com o valor procurado, eliminando a metade da lista que não contém o valor procurado e repetindo o processo até encontrar o valor.
- `O(log n)`

### Exercício 1.1

Como o número de etapas pode ser calculado pelo logaritmo de n na base 2 e o número é 128, a quantidade de etapas é 7.

### Exercício 1.2

Como pede para dobrar o tamanho da lista e a base do logaritmo é 2, o número de etapas aumenta em 1, no caso, 8.
