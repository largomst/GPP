class Monster:
    def __init__(self, breed: Breed):
        self._health = breed.getHealth()
        self._breed = breed

    def getAttack(self):
        if self._health < LOW_HEALTH:
            return "The monster fails weakly."

    def getBreed(self):
        "Breed 本质上一个类型，而 Monster 是无类型的——需要实例化才能使用。"
        return self._breed


class Breed:
    def __init__(
        self, health: int = None, attack: function = None, parent: Breed = None
    ):
        if parent is not None:
            if health == 0:
                self._health = parent.getHealth()
            if attack is None:
                self._attack = parent.getAttack()

    def newMonster(self):
        """
        产生新 Moster 实例的工厂方法，使用“类型”来产生一个类型
        """
        return Monster(self)

    def getHealth(self):
        return self._health

    def getAttack(self):
        return self._attack

