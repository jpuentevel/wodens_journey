"""
*** V_0.1.3 ***

Falta implementar por ahora:

- Si un efecto actúa sobre un personaje que ya tenía un efecto sobre sí,
  debe prevalecer el efecto ganador según su tipo.

- Si un efecto actúa sobre un personaje que ya tenía un efecto sobre sí,
  el nuevo efecto debe tener el contador de turnos (shifts) reiniciado
  para se efectúe durante el número de turnos que le corresponde (3).

- Más cosas que salgan por el camino.

"""

import random
# random.randint(0, 100) -> número aleatorio del 0 al 100


class Character:
    def __init__(self, name, life, damage):
        self.name = name
        self.life = life
        self.damage = damage
        self.has_an_effect = False

    def print_stats(self):
        print(f"Nombre: {self.name}")
        print(f"HP: {self.life}")
        print(" ")

    def set_attack(self, attack):
        self.attack = attack

    def get_damage(self, attack):
        self.life = self.life - attack
        if self.life < 0:
            self.life = 0


class Attack:
    def __init__(self, element, base_damage, element_damage, critic_damage, critic_prob, miss_prob):
        self.element = element
        self.base_damage = base_damage
        self.element_damage = element_damage
        self.critic_damage = critic_damage
        self.critic_prob = critic_prob
        self.miss_prob = miss_prob
        self.critic_attack = False
        self.elemental_attack = False

    def get_element_name(self):
        if self.element == 1:
            self.element_name = "FIRE"
            self.elemental_attack = True

        elif self.element == 2:
            self.element_name = "WATER"
            self.elemental_attack = True

        elif self.element == 3:
            self.element_name = "ICE"
            self.elemental_attack = True

        else:
            self.element_name = "NORMAL"
            self.elemental_attack = False

    def its_critic(self, number_for_probs):
        if number_for_probs <= self.critic_prob:
            self.critic_attack = True

        else:
            self.critic_attack = False

        return self.critic_attack

    def attack_missed(self, number_for_probs):
        if number_for_probs <= self.miss_prob:
            return True
        else:
            return False

    def calc_damage_attack(self):
        if self.attack_missed(random.randint(0, 100)) == False:

            self.damage = self.base_damage

            if self.element == 1 or self.element == 2 or self.element == 3:
                self.damage = self.damage + self.element_damage

            if self.its_critic(random.randint(0, 100)) == True:
                self.damage = self.damage + self.critic_damage
                print(" ")
                print("¡EL ATAQUE HA SIDO CRÍTICO!")
                print(" ")

        else:
            self.damage = 0
            print(" ")
            print("¡EL ATAQUE HA FALLADO!")
            print(" ")

        print(f"¡EL ATAQUE HA INFLIGIDO {self.damage} DE DAÑO!")
        print(" ")


class Effect:
    def __init__(self, element):
        self.element = element

    def elemental_effect(self, name, shifts, miss_prob, freeze):
        if self.element == "FIRE":
            """
            Aplica QUEMADURA (versión en Inglés está por revisar):
            Quita 20HP (aún está por revisar) cantidad de vida durante 3 turnos.
            """
            if shifts > 0:
                shifts = shifts - 1
                damage = 20
                print(" ")
                print(f"¡{name} está bajo efecto de QUEMADURA!")
                print(
                    f"¡La QUEMADURA ha aplicado {damage} Puntos de daño a {name}!")
                print(f"¡{shifts} rondas de QUEMADURA restantes!")
                print(" ")
                return self.element, damage, shifts
            else:
                print(" ")
                print(f"¡{name} ya no está bajo efecto de QUEMADURA!")
                print(" ")
                return self.element, False

        elif self.element == "WATER":
            """
            Aplica TSUNAMI (versión en Inglés está por revisar):
            "Arrastra" al enemigo a una gran distancia, reduciendo su precisión,
            aumentando su probabilidad de fallar en 60 Puntos (aún está por revisar).
            """
            if shifts > 0:
                if shifts == 3:
                    miss_prob = miss_prob + 60
                shifts = shifts - 1
                print(" ")
                print(f"¡{name} fue arrojado por TSUNAMI!")
                print(
                    f"¡La probabilidad de fallar de {name} pasa a {miss_prob} Puntos!")
                print(f"¡{shifts} rondas de TSUNAMI restantes!")
                print(" ")
                return self.element, miss_prob, shifts
            else:
                print(" ")
                print(f"¡{name} ya salió del efecto de TSUNAMI!")
                print(
                    f"¡La probabilidad de fallar de {name} vuelve a la normalidad!")
                print(" ")
                return self.element, False

        elif self.element == "ICE":
            """
            Aplica CONGELAMIENTO (versión en Inglés está por revisar):
            "Congela" al rival, lo que le impide hacer algo durante el
            siguiente turno.
            """
            if freeze == False:
                print(" ")
                print(f"¡{name} está bajo efecto de CONGELAMIENTO!")
                print(f"¡{name} no puede hacer nada durante este turno!")
                print(" ")
                freeze = True
                
            else:
                print(" ")
                print(f"¡{name} ya no está bajo efecto de CONGELAMIENTO!")
                print(" ")
                freeze = False
            
            return self.element, freeze


if __name__ == '__main__':
    woden = Character("Woden", 200, 10)
    enemy = Character("Enemy", 200, 10)

    # Shift starts
    while True:
        print(" ")
        print("*** COMIENZA EL TURNO ***")
        print(" ")

        # Woden's attack
        if woden.has_an_effect == True:

            # Recibe el tipo de ataque, la vida y el número de turnos
            w_effect_stats = w_effect.elemental_effect(
                woden.name, w_shifts, w_attack.miss_prob, w_freeze)
            
            if w_effect_stats[1] != False:

                if w_effect_stats[0] == "FIRE":
                    damage = w_effect_stats[1]
                    woden.get_damage(damage)
                    w_shifts = w_effect_stats[2]

                elif w_effect_stats[0] == "WATER":
                    miss_prob = w_effect_stats[1]
                    w_shifts = w_effect_stats[2]

                elif w_effect_stats[0] == "ICE":
                    w_freeze = w_effect_stats[1]
                    print("*** ENTRA EN EFECTO ICE ***")

            else:
                woden.has_an_effect = False

        else:
            miss_prob = 20
            w_shifts = 3
            w_freeze = False

        woden.print_stats()

        # Si Woden no está congelado puede atacar
        if w_freeze == False:
            while True:
                print("1. Ataque normal.")
                print("2. Ataque elemental.")
                opc = int(input("¿Qué desea hacer?: "))
                print(" ")

                if opc == 1:
                    atk = 0
                    break
                elif opc == 2:
                    atk = 1
                    break

            if atk == 1:
                while True:
                    print("1. Fuego.")
                    print("2. Agua.")
                    print("3. Hielo.")
                    opc = int(input("¿Qué desea hacer?: "))
                    print(" ")

                    if opc == 1:
                        atk = 1
                        break
                    elif opc == 2:
                        atk = 2
                        break
                    elif opc == 3:
                        atk = 3
                        break

            w_attack = Attack(atk, woden.damage, 20, 10, 30, miss_prob)
            w_attack.get_element_name()

        # Enemy's attack
        if enemy.has_an_effect == True:

            # Recibe el tipo de ataque, la vida y el número de turnos
            e_effect_stats = e_effect.elemental_effect(
                enemy.name, e_shifts, e_attack.miss_prob, e_freeze)
            
            if e_effect_stats[1] != False:
                 
                if e_effect_stats[0] == "FIRE":
                    damage = e_effect_stats[1]
                    enemy.get_damage(damage)
                    e_shifts = e_effect_stats[2]

                elif e_effect_stats[0] == "WATER":
                    miss_prob = e_effect_stats[1]
                    e_shifts = e_effect_stats[2]

                elif e_effect_stats[0] == "ICE":
                    e_freeze = e_effect_stats[1]

            else:
                enemy.has_an_effect = False

        else:
            miss_prob = 20
            e_shifts = 3
            e_freeze = False

        enemy.print_stats()

        # Si Enemy no está congelado puede atacar
        if e_freeze == False:
            atk = random.randint(0, 3)
            e_attack = Attack(atk, woden.damage, 20, 10, 30, miss_prob)
            e_attack.get_element_name()

        # Elementos de los ataques
        print(" ")
        # Si Woden no está congelado, se muestra su tipo de ataque
        if w_freeze == False:
            print(
                f"¡WODEN HA USADO UN ATAQUE DE TIPO {w_attack.element_name}!")
        # Si Enemy no está congelado, se muestra su tipo de ataque
        if e_freeze == False:
            print(
                f"¡EL ENEMIGO HA USADO UN ATAQUE DE TIPO {e_attack.element_name}!")
        print(" ")

        # ¿Quién gana el turno?

        # Si ninguno está congelado, se evalúan los tipos de los ataques
        if w_freeze == False and e_freeze == False:

            if w_attack.element_name == "FIRE" and e_attack.element_name == "FIRE":
                woden_wins_shift = True
                enemy_wins_shift = True

            elif w_attack.element_name == "FIRE" and e_attack.element_name == "WATER":
                woden_wins_shift = False
                enemy_wins_shift = True

            elif w_attack.element_name == "FIRE" and e_attack.element_name == "ICE":
                woden_wins_shift = True
                enemy_wins_shift = False

            elif w_attack.element_name == "WATER" and e_attack.element_name == "WATER":
                woden_wins_shift = True
                enemy_wins_shift = True

            elif w_attack.element_name == "WATER" and e_attack.element_name == "FIRE":
                woden_wins_shift = True
                enemy_wins_shift = False

            elif w_attack.element_name == "WATER" and e_attack.element_name == "ICE":
                woden_wins_shift = False
                enemy_wins_shift = True

            elif w_attack.element_name == "ICE" and e_attack.element_name == "ICE":
                woden_wins_shift = True
                enemy_wins_shift = True

            elif w_attack.element_name == "ICE" and e_attack.element_name == "FIRE":
                woden_wins_shift = False
                enemy_wins_shift = True

            elif w_attack.element_name == "ICE" and e_attack.element_name == "WATER":
                woden_wins_shift = True
                enemy_wins_shift = False

            elif w_attack.element_name == "NORMAL" or e_attack.element_name == "NORMAL":
                woden_wins_shift = True
                enemy_wins_shift = True
        
        # Si Woden no está congelado pero el enemigo sí:
        elif w_freeze == False and e_freeze == True:
            woden_wins_shift = True
            enemy_wins_shift = False

        # Si Woden está congelado pero el enemigo no:
        elif w_freeze == True and e_freeze == False:
            woden_wins_shift = False
            enemy_wins_shift = True
        
        # Si ambos están congelados:
        else:
            woden_wins_shift = False
            enemy_wins_shift = False

        if woden_wins_shift == True:
            print("¡WODEN HA GANADO EL TURNO!")
            w_attack.calc_damage_attack()
            woden.set_attack(w_attack.damage)
            enemy.get_damage(woden.attack)
            print(f"Enemy HP: {enemy.life}")
            print(" ")
            if w_attack.critic_attack == True and w_attack.elemental_attack == True:
                enemy.has_an_effect = True
                e_effect = Effect(w_attack.element_name)

        if enemy_wins_shift == True:
            print("¡EL ENEMIGO HA GANADO EL TURNO!")
            e_attack.calc_damage_attack()
            enemy.set_attack(e_attack.damage)
            woden.get_damage(enemy.attack)
            print(f"Woden HP: {woden.life}")
            print(" ")
            if e_attack.critic_attack == True and e_attack.elemental_attack == True:
                woden.has_an_effect = True
                w_effect = Effect(e_attack.element_name)

        # Quitamos FREEZE al final del turno
        if w_freeze == True:
            w_freeze = False
            woden.has_an_effect = False

        if e_freeze == True:
            e_freeze = False
            enemy.has_an_effect = False

        print(" ")
        print("*** FIN DEL TURNO ***")
        print(" ")

        if woden.life == 0:
            print(" ")
            print("¡WODEN HA MUERTO!")
            print("¡EL ENEMIGO HA GANADO EL COMBATE!")
            print(" ")
            break
        elif enemy.life == 0:
            print(" ")
            print("¡EL ENEMIGO HA MUERTO!")
            print("¡WODEN HA GANADO EL COMBATE!")
            print(" ")
            break
