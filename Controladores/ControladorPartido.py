from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Resultados.Partido import Partido

class ControladorPartido():

    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        partido = Partido(infoPartido)
        return self.repositorioPartido.save(partido)

    def update(self, id, infoPartido):
        partido = Partido(self.repositorioPartido.findById(id))
        partido.lema = infoPartido['lema']
        partido.nombre = infoPartido['nombre']
        return self.repositorioPartido.save(partido)

    def delete(self, id):
        print("Eliminando el partido con id: ", id)
        return {"deleted_count": 1}

    def show(self, id):
        partido = Partido(self.repositorioPartido.findById(id))
        return partido.__dict__