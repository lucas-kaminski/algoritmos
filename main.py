import argparse
import os
import sys
import subprocess
from utils import logger


parser = argparse.ArgumentParser(description="Gerenciador dos scripts.")
parser.add_argument(
    "-v", "--verbose", help="Mostra mais informações", action="store_true"
)

args = parser.parse_args()
if args.verbose:
    os.environ.setdefault("DEBUG", "AAA")


def main():
    simbolos_proibidos = [".", "_", "-"]
    capitulos = [
        f
        for f in os.listdir(".")
        if os.path.isdir(f) and f[0] not in simbolos_proibidos
    ]
    escolha_usuario = None
    capitulo_escolhido = None

    while capitulo_escolhido not in capitulos:
        logger.info("Escolha um capítulo:")
        for capitulo in enumerate(capitulos):
            logger.info(f"{capitulo[0]} - {capitulo[1]}")
        escolha_usuario = input("-> ")
        try:
            capitulo_escolhido = capitulos[int(escolha_usuario)]
        except (IndexError, ValueError):
            logger.info("Capítulo inválido!")
            continue

    caminho_capitulo = os.path.join(os.getcwd(), capitulo_escolhido)
    algoritmos = [f for f in os.listdir(caminho_capitulo)]
    escolha_usuario = None
    algoritmo_escolhido = None

    while algoritmo_escolhido not in algoritmos:
        logger.info("Escolha um algoritmo:")
        for algoritmo in enumerate(algoritmos):
            logger.info(f"{algoritmo[0]} - {algoritmo[1]}")
        escolha_usuario = input("-> ")
        try:
            algoritmo_escolhido = algoritmos[int(escolha_usuario)]
        except (IndexError, ValueError):
            logger.info("Algoritmo inválido!")
            continue

    logger.info(f"Executando {algoritmo_escolhido}...")
    logger.info("---\n")
    caminho_algoritmo = os.path.join(caminho_capitulo, algoritmo_escolhido)
    subprocess.run(
        ["python", caminho_algoritmo],
        env=dict(os.environ, PYTHONPATH=os.getcwd()),
    )
    logger.info("\n---")

    escolha_final = None
    escolhas = ["Repetir", "Reiniciar", "Sair"]
    while escolha_final not in escolhas:
        for escolha in enumerate(escolhas):
            logger.info(f"{escolha[0]} - {escolha[1]}")
        escolha_final = input("-> ")
        try:
            escolha_final = escolhas[int(escolha_final)]
            if escolha_final == "Repetir":
                logger.info("---\n")
                subprocess.run(
                    ["python", caminho_algoritmo],
                    env=dict(os.environ, PYTHONPATH=os.getcwd()),
                )
                logger.info("\n---")
                escolha_final = None
            elif escolha_final == "Reiniciar":
                main()
            elif escolha_final == "Sair":
                sys.exit(0)
        except (IndexError, ValueError):
            logger.info("Escolha inválida!")
            sys.exit(0)


if __name__ == "__main__":
    main()
