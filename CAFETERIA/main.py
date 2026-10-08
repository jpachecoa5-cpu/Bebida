from gestor import GestorCafeteria
from models.capuccino import Capuccino
from models.mocaccino import Mocaccino


def main():
    gestor = GestorCafeteria()
    gestor.agregar_bebida(Capuccino(30, "mediano"))
    gestor.agregar_bebida(Mocaccino(35, "grande"))

    print("MENÚ DE CAFETERÍA")
    print(gestor.mostrar_menu())


if __name__ == "__main__":
    main()
