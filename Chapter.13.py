class Monster:
    def __init__(self, breed: Breed):
        self._health = breed.getHealth()
        self._breed = breed

    def getAttack(self):
        return self._breed.getAttack()


class Breed:
    def __init__(
        self, health: int = None, attack: function = None, parent: Breed = None
    ):
        self._parent = parent  # 用 parent 来实现非面向对象机制的派生机制。
        self._health = health
        self._attack = attack

    def newMonster(self):
        """
        产生新 Moster 实例的工厂方法，使用“类型”来产生一个类型
        """
        return Monster(self)

    def getHealth(self):
        if self._health != 0 or self._parent == None:
            return self._health
        else:
            return self._parent._health

    def getAttack(self):
        if self._attack != None or self._parent == None:
            return self._attack
        else:
            return self._parent._attack

