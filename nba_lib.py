
import random
from power import Skills
# Object players 

class JugardorClass(object):
    # attributes
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

    def process_return_posicion_of_players(self):
        return self.posicion_del_jugador

    def process_return_capacity_of_players(self):
        return self.capacidad_del_jugador

    def process_return_skill(self):
        return self.skill

# Object teams
class EquipoClass(object):
    def __init__(self, nombre_del_equipo):
        self.nombre_equipo = nombre_del_equipo
        self.jugadores = []

    def process_save_players(self, jugador):
        self.jugadores.append(jugador)
        return 0
    def __str__(self):
        return str("objeto equipo: "+self.nombre_equipo)

    def process_quantity_of_players(self):
        return len(self.jugadores)

    def process_return_players(self):
        return self.jugadores

    def process_return_name_of_the_team(self):
        return self.nombre_equipo
# object league
class LigaNBA(object):
    def __init__(self):
        self.equipo_seleccionado_en_la_ligaNBA = []
        self.equipo_almacenado = []
        self.contador = 0

    def process_quantity_league(self):
        longitut = len(self.equipo_seleccionado_en_la_ligaNBA)
        return longitut

    def process_save_league(self, equipo):
        self.equipo_seleccionado_en_la_ligaNBA.append(equipo)

    def process_print_league(self):
        for i in self.equipo_seleccionado_en_la_ligaNBA:
            print i
        return 0
    def process_return_league(self):
       return self.equipo_seleccionado_en_la_ligaNBA
