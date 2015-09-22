import random
from power import Skills
# Object players 

class PlayersClass(object):
    # members
    def __init__(self, identificador,nombre,numero,link):
        self.id = identificador
        self.nombre = nombre
        self.dorsal = numero
        self.posicion = ""
        self.equipo = ""
        self.dorsal = ""
         # List
        self.posicion_del_jugador = ['Alero', 'Pivot', 'Base']
         # dictionary
        self.capacidad_del_jugador = {'Tiros': random.randrange(0, 100), 'Ataque': random.randrange(0, 100),
                                 'Pases': random.randrange(0, 100), 'Rebotes': random.randrange(0, 100),
                                 'Defense': random.randrange(0, 100)}
        self.photo = link
    def process_add_team(self, nombre_equipo):
        self.equipo = nombre_equipo
        return self.equipo

    def process_return_name_of_players(self):
        return self.nombre

    def process_return_image(self):
        return self.photo

    def process_generate_skill(self):
    		# instantiate
        self.almacenar_skill(Skills(random.choice(self.posicion_del_jugador[random.randrange(0,3)]),self.capacidad_del_jugador))

    def process_save_skill(self,skill):
         self.skill = skill

    def process_return_posicion_of_the_players(self):
        return self.posicion_del_jugador

    def process_return_capacity_of_players(self):
        return self.capacidad_del_jugador

    def process_return_skill(self):
        return self.skill
