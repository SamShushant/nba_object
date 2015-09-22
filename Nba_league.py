# object league
class NbaLeagueClass(object):
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
