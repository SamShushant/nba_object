class TeamsClass(object):
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
