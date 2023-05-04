class Effect:

    def __init__(self, element):

        self.element = element
    
    def element_effect(self, name, turns, damage, miss_prob, freeze):

        if self.element == "FIRE":

            """
            Aplica QUEMADURA (versión en Inglés está por revisar):
            Quita 20HP (aún está por revisar) cantidad de vida durante 3 turnos.
            """

            if turns > 0:

                turns = turns - 1
                print(" ")
                print(f"¡{name} está bajo efecto de QUEMADURA!")
                print(f"¡La QUEMADURA ha aplicado {damage} Puntos de daño a {name}!")
                print(f"¡{turns} turnos de QUEMADURA restantes!")
                print(" ")
                return self.element, True, damage, turns
            
            else:

                print(" ")
                print(f"¡{name} ya no está bajo efecto de QUEMADURA!")
                print(" ")
                return self.element, False, 0, 0
        
        elif self.element == "WATER":

            """
            Aplica TSUNAMI (versión en Inglés está por revisar):
            "Arrastra" al enemigo a una gran distancia, reduciendo su precisión,
            aumentando su probabilidad de fallar en 60 Puntos (aún está por revisar).
            """
            
            if turns > 0:
                
                if turns == 3:

                    miss_prob = miss_prob + 60
                
                turns = turns - 1
                print(" ")
                print(f"¡{name} fue arrojado por TSUNAMI!")
                print(f"¡La probabilidad de fallar de {name} pasa a {miss_prob} Puntos!")
                print(f"¡{turns} turnos de TSUNAMI restantes!")
                print(f" ")
                return self.element, True, miss_prob, turns
            
            else:

                print(" ")
                print(f"¡{name} ya no está bajo efecto de TSUNAMI!")
                print(f"¡La probabilidad de fallar de {name} vuelve a la normalidad!")
                print(" ")
                return self.element, False, 0, 0
        
        elif self.element == "ICE":

            """
            Aplica CONGELAMIENTO (versión en Inglés está por revisar):
            "Congela" al rival, lo que le impide hacer algo durante el
            siguiente turno.
            """

            if not freeze:

                print(" ")
                print(f"¡{name} está bajo efecto de CONGELAMIENTO!")
                print(f"¡{name} no puede hacer nada durante este turno!")
                print(" ")
                freeze = True
            
            else:

                print(" ")
                print(f"¡{name} ya está bajo efecto de CONGELAMIENTO!")
                print(" ")
                freeze = False
            
            return self.element, freeze, 0, 0
        
        else:

            return "NORMAL", False, 0, 0