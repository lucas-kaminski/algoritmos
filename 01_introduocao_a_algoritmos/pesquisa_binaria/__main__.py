import random
import math
from utils import logger


def pesquisa_binaria(lista, item):
    logger.debug(f"Máximo de etapas: {math.ceil(math.log(len(lista), 2))}")

    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


minha_lista = [1, 3, 5, 7, 9]

logger.info(pesquisa_binaria(minha_lista, 3))

logger.info(pesquisa_binaria(minha_lista, -1))


logger.info("")

lista_aleatoria = [random.randint(1, 100) for _ in range(256)]
lista_aleatoria.sort()

numero_aleatorio = random.randint(1, 100)
# numero_aleatorio = random.choice(lista_aleatoria)

logger.info(
    f"O número {numero_aleatorio} está na posição {pesquisa_binaria(lista_aleatoria, numero_aleatorio)}"
)
