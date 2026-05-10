class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if self._health < 0:
            raise ValueError('Health cannot be below 0.')
        if  self.health > 100:
            raise ValueError('Health cannot be more than 100.')
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if self._mana < 0:
            raise ValueError
        if self._mana > 50:
            raise ValueError
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self._name} leveled up to {self._level}!')

    def __str__(self):
        return f'''Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}'''

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)