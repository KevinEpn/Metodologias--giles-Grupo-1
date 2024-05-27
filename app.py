class JuegoCruceRio:
    def __init__(self):
        self.lado_izquierdo = {'Lobo', 'Caperucita', 'Uvas', 'Vikingo'}
        self.lado_derecho = set()
        self.balsa = set()

    def mostrar_estado(self):
        print(f"\nLado Izquierdo: {self.lado_izquierdo}\nLado Derecho: {self.lado_derecho}\nBalsa: {self.balsa}\n")

    def verificar_restricciones(self, lado):
        if ('Caperucita' in lado and 'Uvas' in lado and 'Vikingo' not in lado) or ('Lobo' in lado and 'Caperucita' in lado and 'Vikingo' not in lado):
            print("\n¡Caperucita se comió las uvas!" if 'Uvas' in lado else "¡El lobo se comió a Caperucita!", "\n¡Juego terminado!")
            return False
        return True

    def mover_personajes(self, lado_origen, lado_destino, personajes_a_mover):
        if len(personajes_a_mover) > 2:
            print("\nNo puedes mover más de 2 personajes a la vez.")
            return False

        for personaje in personajes_a_mover:
            if personaje not in lado_origen:
                print(f"\n{personaje} no está en el lado correcto.")
                return False

        for personaje in personajes_a_mover:
            lado_origen.remove(personaje)
            self.balsa.add(personaje)

        self.simular_navegacion()

        for personaje in personajes_a_mover:
            self.balsa.remove(personaje)
            lado_destino.add(personaje)

        return True

    def simular_navegacion(self):
        print("Navegando" + "." * 10 + "\n")

    def jugar(self):
        while True:
            self.mostrar_estado()
            if len(self.lado_derecho) == 4:
                print("\n¡Todos los personajes han cruzado el río exitosamente!")
                break

            personajes_a_mover = [personaje.strip().capitalize() for personaje in input("\nIngresa los personajes a mover separados por una coma: ").split(',')]

            if any(personaje not in self.lado_izquierdo and personaje not in self.lado_derecho for personaje in personajes_a_mover):
                print("\nUno o más personajes ingresados no son válidos.")
                continue

            if 'Vikingo' in self.lado_izquierdo:
                if self.mover_personajes(self.lado_izquierdo, self.lado_derecho, personajes_a_mover):
                    if not self.verificar_restricciones(self.lado_izquierdo):
                        break
            else:
                if self.mover_personajes(self.lado_derecho, self.lado_izquierdo, personajes_a_mover):
                    if not self.verificar_restricciones(self.lado_derecho):
                        break

if __name__ == "__main__":
    juego = JuegoCruceRio()
    juego.jugar()