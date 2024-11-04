from equipe.diagramadores_equipe import EquipeDiagramadores
from equipe.documentadores_equipe import EquipeDocumentadores

from typing import  Dict

class AutoDocController:
    def __init__(self):       
        
        self.documentadores = EquipeDocumentadores().crew()
        self.diagramadores = EquipeDiagramadores().crew()

    def run_documentadores(self, inputs: Dict[str, str]):               
        crew_result = self.documentadores.kickoff(inputs=inputs)
        
        return crew_result

    def run_diagramadores(self, inputs: Dict[str, str]):               
        crew_result = self.diagramadores.kickoff(inputs=inputs)
        
        return crew_result

    