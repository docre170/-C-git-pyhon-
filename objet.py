class Player:
    # un objet s'agit des element 
    # un attribut
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("bienvenue au joueur", pseudo, "  /points de vie: ", health,"/attaque", attack)
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack_value(self):
        return self.attack
    
    def damage(self, damage):
        self.health -= damage
    
    def attack_player(self, target_player):
        target_player.damage(self.attack)
    
player = Player("graven", 20,2)
player.damage(3)