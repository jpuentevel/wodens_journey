class Character:
    
    def __init__(self, name, life, damage):
        
        self.name = name
        self.life = life
        self.damage = damage
        self.has_an_effect = False
        self.attack = 0
    
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