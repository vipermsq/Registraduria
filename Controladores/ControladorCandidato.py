from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Resultados.Candidato import Candidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Resultados.Partido import  Partido

class ControladorCandidato():

    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        candidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(candidato)

    def update(self, id, infoCandidato):
        candidato = Candidato(self.repositorioCandidato.findById(id))
        candidato.cedula = infoCandidato['cedula']
        candidato.numero_resolucion = infoCandidato['numero_resolucion']
        candidato.nombre = infoCandidato['nombre']
        candidato.apellido = infoCandidato['apellido']
        return self.repositorioCandidato.save(candidato)

    def delete(self, id):
        self.repositorioCandidato.delete(id)
        print("Eliminando el candidato con id: ", id)
        return {"deleted_count": 1}

    def show(self, id):
        candidato = Candidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__

    def setPartido(self, id_candidato, id_partido):
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        partido = Partido(self.repositorioPartido.findById(id_partido))
        candidato.partido = partido
        return self.repositorioCandidato.save(candidato)
