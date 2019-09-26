class Monster:
    def __init__(self, startingHealth: int):
        self._heath = startingHealth

    def getAttack(self):
        return 0


class Dragon(Monster):
    def __init__(self, startingHealth=230):
        super().__init__(startingHealth)

    def getAttack(self):
        return "The dragon breathes fire!"


class Troll(Monster):
    def __init__(self, startingHealth=48):
        super().__init__(startingHealth)

    def getAttack(self):
        return "The troll clubs you!"

