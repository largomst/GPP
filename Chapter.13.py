class Monster:
    def __init__(self, breed: Breed):
        self._heath = breed.getHealth()
        self._breed = breed

    def getAttack(self):
        return self._breed.getAttack()


class Breed:
    def __init__(self, health: int, attack: function):
        self._health = health
        self._attack = attack

    def getHealth(self):
        return self._health

    def getAttack(self):
        return self._attack

