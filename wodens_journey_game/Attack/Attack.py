import random

class Attack:

    def __init__(self, element, base_damage, element_damage, critic_damage, critic_prob, miss_prob):
        
        self.element = element
        self.base_damage = base_damage
        self.element_damage = element_damage
        self.critic_damage = critic_damage
        self.critic_prob = critic_prob
        self.miss_prob = miss_prob
        self.element_name = ""
        self.damage = 0
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
            
            self.critic_attack = True
        
        return self.critic_attack
    
    def attack_missed(self, number_for_probs):

        if number_for_probs <= self.miss_prob:

            return True
        
        else:
            
            return False
    
    def calc_damage_attack(self):

        if not self.attack_missed(random.randint(0, 100)):

            self.damage = self.base_damage

            if self.element == 1 or self.element == 2 or self.element == 3:
                
                self.damage += self.element_damage
            
            if self.its_critic(random.randint(0, 100)):
                
                self.damage += self.critic_damage
                print(" ")
                print("¡EL ATAQUE HA SIDO CRÍTICO!")
                print(" ")
        
        else:

            self.damage = 0
            print(" ")
            print("¡EL ATAQUE HA FALLADO!")
            print(" ")
        
        print(f"¡EL ATAQUE HA INFLIGIDO {self.damage} DE DAÑO!")