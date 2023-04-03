import random
# random.randint(0, 100)

class Character:
    def __init__(self, name, life, damage):
        self.name = name
        self.life = life
        self.damage = damage

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

    def get_element_name(self):
        if self.element == 1:
            self.element_name = "FIRE"
        elif self.element == 2:
            self.element_name = "WATER"
        elif self.element == 3:
            self.element_name = "ICE"
        else:
            self.element_name = "NORMAL"

    def its_critic(self, number_for_probs):
        if number_for_probs <= self.critic_prob:
            return True
        else:
            return False

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

        print(" ")
        print(f"¡EL ATAQUE HA INFLIGIDO {self.damage} DE DAÑO!")
        print(" ")
                


if __name__ == '__main__':
    woden = Character("Woden", 200, 10)
    enemy = Character("Enemy", 200, 10)

    # Turn
    while True:
        print(" ")
        print("*** COMIENZA EL TURNO ***")
        print(" ")
        # Woden's attack
        while True:
            woden.print_stats()
            print("1. Ataque normal.")
            print("2. ataque elemental.")
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

        w_attack = Attack(atk, woden.damage, 20, 10, 30, 20)
        w_attack.get_element_name()
        

        # Enemy's attack
        enemy.print_stats()
        atk = random.randint(0, 3)
        e_attack = Attack(atk, woden.damage, 20, 10, 30, 20)
        e_attack.get_element_name()
        
        # Elementos de los ataques
        print(" ")
        print(f"¡WODEN HA USADO UN ATAQUE DE TIPO {w_attack.element_name}!")
        print(f"¡EL ENEMIGO HA USADO UN ATAQUE DE TIPO {e_attack.element_name}!")
        print(" ")

        # ¿Quién gana el turno?
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
        
        if woden_wins_turn == True:
            print("¡WODEN HA GANADO EL TURNO!")
            w_attack.calc_damage_attack()
            woden.set_attack(w_attack.damage)
            enemy.get_damage(woden.attack)
            print(f"Enemy HP: {enemy.life}")
            print(" ")
        
        if enemy_wins_turn == True:
            print("¡EL ENEMIGO HA GANADO EL TURNO!")
            e_attack.calc_damage_attack()
            enemy.set_attack(e_attack.damage)
            woden.get_damage(enemy.attack)
            print(f"Woden HP: {woden.life}")
            print(" ")

        
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
            print("¡EL ENEMY HA MUERTO!")
            print("¡WODEN HA GANADO EL COMBATE!")
            print(" ")
            break

