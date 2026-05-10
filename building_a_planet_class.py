class Planet:
    def __init__(self, name, planet_type, star):
        para = (name, planet_type, star)
        for i in para:
            if not isinstance(i, str):
                raise TypeError ('name, planet type, and star must be strings')
            if len(i) == 0:
                raise ValueError ('name, planet_type, and star must be non-empty strings')

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1= Planet('Earth', 'Habitable', 'Sun')
planet_2= Planet('Kepler-186f', 'Habitable', 'Kepler-186')
planet_3= Planet('Saturn', 'Non-habitable', 'Sun')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())