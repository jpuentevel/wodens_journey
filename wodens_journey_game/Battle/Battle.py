from Character.Character import Character
from Attack.Attack import Attack
from Effect.Effect import Effect
import random


class Battle:

    def __init__(self, hero_name, hero_life, hero_damage, hero_elemental_damage, hero_critic_damage, hero_critic_prob,
                 hero_miss_prob, enemy_name, enemy_life, enemy_damage, enemy_elemental_damage, enemy_critic_damage,
                 enemy_critic_prob, enemy_miss_prob, ):

        self.hero_name = hero_name
        self.hero_life = hero_life
        self.hero_damage = hero_damage
        self.hero_elemental_damage = hero_elemental_damage
        self.hero_critic_damage = hero_critic_damage
        self.hero_critic_prob = hero_critic_prob
        self.hero_miss_prob = hero_miss_prob

        self.enemy_name = enemy_name
        self.enemy_life = enemy_life
        self.enemy_damage = enemy_damage
        self.enemy_elemental_damage = enemy_elemental_damage
        self.enemy_critic_damage = enemy_critic_damage
        self.enemy_critic_prob = enemy_critic_prob
        self.enemy_miss_prob = enemy_miss_prob

    def battle_start(self):

        woden = Character(self.hero_name, self.hero_life, self.hero_damage)
        enemy = Character(self.enemy_name, self.enemy_life, self.enemy_damage)

        while True:

            print(" ")
            print("*** COMIENZA EL TURNO ***")
            print(" ")

            # Woden's attack
            if woden.has_an_effect:

                # Recibe el tipo de ataque, la vida y el número de turnos
                w_effect_stats = w_effect.element_effect(
                    woden.name, w_turns, self.hero_elemental_damage, w_attack.miss_prob, w_freeze)

                if w_effect_stats[1]:

                    if w_effect_stats[0] == "FIRE":
                        damage = w_effect_stats[2]
                        woden.get_damage(damage)
                        w_turns = w_effect_stats[3]

                    elif w_effect_stats[0] == "WATER":
                        miss_prob = w_effect_stats[2]
                        w_turns = w_effect_stats[3]

                    elif w_effect_stats[0] == "ICE":
                        w_freeze = w_effect_stats[1]
                        print("*** ENTRA EN EFECTO ICE ***")

                else:
                    woden.has_an_effect = False

            else:
                miss_prob = self.hero_miss_prob
                w_turns = 3
                w_freeze = False

            woden.print_stats()

            # Si Woden no está congelado puede atacar
            if not w_freeze:
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

                w_attack = Attack(atk, woden.damage, self.hero_elemental_damage, self.hero_critic_damage,
                                  self.hero_critic_prob, miss_prob)
                w_attack.get_element_name()

            # Enemy's attack
            if enemy.has_an_effect:

                # Recibe el tipo de ataque, la vida y el número de turnos
                e_effect_stats = e_effect.element_effect(
                    enemy.name, e_turns, self.enemy_elemental_damage, e_attack.miss_prob, e_freeze)

                if e_effect_stats[1]:

                    if e_effect_stats[0] == "FIRE":
                        damage = e_effect_stats[2]
                        enemy.get_damage(damage)
                        e_turns = e_effect_stats[3]

                    elif e_effect_stats[0] == "WATER":
                        miss_prob = e_effect_stats[2]
                        e_turns = e_effect_stats[3]

                    elif e_effect_stats[0] == "ICE":
                        e_freeze = e_effect_stats[1]

                else:
                    enemy.has_an_effect = False

            else:
                miss_prob = self.enemy_miss_prob
                e_turns = 3
                e_freeze = False

            enemy.print_stats()

            # Si Enemy no está congelado puede atacar
            if not e_freeze:
                atk = random.randint(0, 3)
                e_attack = Attack(atk, woden.damage, self.enemy_elemental_damage, self.enemy_critic_damage,
                                  self.enemy_critic_prob, miss_prob)
                e_attack.get_element_name()

            # Elementos de los ataques
            print(" ")
            # Si Woden no está congelado, se muestra su tipo de ataque
            if not w_freeze:
                print(
                    f"¡WODEN HA USADO UN ATAQUE DE TIPO {w_attack.element_name}!")
            # Si Enemy no está congelado, se muestra su tipo de ataque
            if not e_freeze:
                print(
                    f"¡EL ENEMIGO HA USADO UN ATAQUE DE TIPO {e_attack.element_name}!")
            print(" ")

            # ¿Quién gana el turno?
            # Si ninguno está congelado, se evalúan los tipos de los ataques
            if w_freeze == False and e_freeze == False:

                if w_attack.element_name == "FIRE" and e_attack.element_name == "FIRE":
                    woden_wins_turn = True
                    enemy_wins_turn = True

                elif w_attack.element_name == "FIRE" and e_attack.element_name == "WATER":
                    woden_wins_turn = False
                    enemy_wins_turn = True

                elif w_attack.element_name == "FIRE" and e_attack.element_name == "ICE":
                    woden_wins_turn = True
                    enemy_wins_turn = False

                elif w_attack.element_name == "WATER" and e_attack.element_name == "WATER":
                    woden_wins_turn = True
                    enemy_wins_turn = True

                elif w_attack.element_name == "WATER" and e_attack.element_name == "FIRE":
                    woden_wins_turn = True
                    enemy_wins_turn = False

                elif w_attack.element_name == "WATER" and e_attack.element_name == "ICE":
                    woden_wins_turn = False
                    enemy_wins_turn = True

                elif w_attack.element_name == "ICE" and e_attack.element_name == "ICE":
                    woden_wins_turn = True
                    enemy_wins_turn = True

                elif w_attack.element_name == "ICE" and e_attack.element_name == "FIRE":
                    woden_wins_turn = False
                    enemy_wins_turn = True

                elif w_attack.element_name == "ICE" and e_attack.element_name == "WATER":
                    woden_wins_turn = True
                    enemy_wins_turn = False

                elif w_attack.element_name == "NORMAL" or e_attack.element_name == "NORMAL":
                    woden_wins_turn = True
                    enemy_wins_turn = True

            # Si Woden no está congelado pero el enemigo sí:
            elif w_freeze == False and e_freeze == True:
                woden_wins_turn = True
                enemy_wins_turn = False

            # Si Woden está congelado pero el enemigo no:
            elif w_freeze == True and e_freeze == False:
                woden_wins_turn = False
                enemy_wins_turn = True

            # Si ambos están congelados:
            else:
                woden_wins_turn = False
                enemy_wins_turn = False

            if woden_wins_turn:
                print("¡WODEN HA GANADO EL TURNO!")
                w_attack.calc_damage_attack()
                woden.set_attack(w_attack.damage)
                enemy.get_damage(woden.attack)
                print(f"Enemy HP: {enemy.life}")
                print(" ")
                if w_attack.critic_attack == True and w_attack.elemental_attack == True:
                    enemy.has_an_effect = True
                    e_effect = Effect(w_attack.element_name)

            if enemy_wins_turn:
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
            if w_freeze:
                w_freeze = False
                woden.has_an_effect = False

            if e_freeze:
                e_freeze = False
                enemy.has_an_effect = False

            print(" ")
            print("*** FIN DEL TURNO ***")
            print(" ")

            if woden.life == 0 and enemy.life == 0:
                print(" ")
                print("¡WODEN Y ENEMY HAN MUERTO A LA VEZ!")
                print("¡HA SIDO UN EMPATE!")
                print(" ")
                break

            elif woden.life == 0 and enemy.life != 0:
                print(" ")
                print("¡WODEN HA MUERTO!")
                print("¡EL ENEMIGO HA GANADO EL COMBATE!")
                print(" ")
                break

            elif woden.life != 0 and enemy.life == 0:
                print(" ")
                print("¡EL ENEMIGO HA MUERTO!")
                print("¡WODEN HA GANADO EL COMBATE!")
                print(" ")
                break
