import random

class Player:

    def __init__(self, name):
        self.player_name = name
        self.health = 100

    def reduce_health(self, damage):
        self.health -= damage

        print(self.player_name + " health left is: " + str(self.health))

    def attack_player(self, player):
        damage = random.randint(1,10)
        print(self.player_name + " attacks " + player.get_name() + " with damage: " + str(damage))
        player.reduce_health(damage)

    def get_name(self):
        return self.player_name

    def is_alive(self):
        return self.health > 0

player1 = Player("Raju")
player2 = Player("Kaju")

print(player1.player_name + " vs " + player2.player_name)

while True:
    player1.attack_player(player2)
    if player2.is_alive() == False:
        print(player1.player_name + " Won!!")
        break
    player2.attack_player(player1)
    if player1.is_alive() == False:
        print(player2.player_name + " Won!!")
        break