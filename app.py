import time
import sys

class JuegoCruceRio:
    def __init__(self):
        self.lado_izquierdo = {'Lobo', 'Caperucita', 'Uvas', 'Observador'}
        self.lado_derecho = set()
        self.balsa = set()

    def mostrar_estado(self):
        print("\nLado Izquierdo: ", self.lado_izquierdo)
        print("Lado Derecho: ", self.lado_derecho)
        print("Balsa: ", self.balsa)
        print("\n")

    def verificar_restricciones(self, lado):
        if 'Caperucita' in lado and 'Uvas' in lado and 'Observador' not in lado:
            print("\n¡Caperucita se comió las uvas!")
            return False
        if 'Lobo' in lado and 'Caperucita' in lado and 'Observador' not in lado:
            print("\n¡El lobo se comió a Caperucita!")
            return False
        return True

    def mover_personajes(self, lado_origen, lado_destino, personajes_a_mover):
        if len(personajes_a_mover) > 2:
            print("\nNo puedes mover más de 2 personajes a la vez.")
            return False

        if any(personaje not in lado_origen for personaje in personajes_a_mover):
            print("\nUno o más personajes no están en el lado correcto.")
            return False

        for personaje in personajes_a_mover:
            lado_origen.remove(personaje)
            self.balsa.add(personaje)

        self.simular_navegacion()

        for personaje in personajes_a_mover:
            self.balsa.remove(personaje)
            lado_destino.add(personaje)

        if not self.verificar_restricciones(lado_origen) or not self.verificar_restricciones(lado_destino):
            print("¡Juego terminado!")
            sys.exit(0)

        return True

    def simular_navegacion(self):
        print("Navegando", end="")
        for _ in range(10):
            time.sleep(0.3)
            print(".", end="")
            sys.stdout.flush()
        print("\n")

    def jugar(self):
        while True:
            self.mostrar_estado()
            if len(self.lado_derecho) == 4:
                print("\n¡Todos los personajes han cruzado el río exitosamente!")
                break

            personajes_a_mover = input("\nIngresa los personajes a mover separados por una coma: ").split(',')
            personajes_a_mover = [personaje.strip().capitalize() for personaje in personajes_a_mover]

            if any(personaje not in self.lado_izquierdo | self.lado_derecho for personaje in personajes_a_mover):
                print("\nUno o más personajes ingresados no son válidos.")
                continue

            if 'Observador' in self.lado_izquierdo or (self.lado_izquierdo & set(personajes_a_mover)):
                self.mover_personajes(self.lado_izquierdo, self.lado_derecho, personajes_a_mover)
            else:
                self.mover_personajes(self.lado_derecho, self.lado_izquierdo, personajes_a_mover)

if __name__ == "__main__":
    juego = JuegoCruceRio()
    juego.jugar()