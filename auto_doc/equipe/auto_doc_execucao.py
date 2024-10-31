from equipe.auto_doc_equipe import EquipeAutoDoc

from typing import  Dict

class AutoDocController:
    def __init__(self):       
        
        self.crew = EquipeAutoDoc().crew()

    def run(self, inputs: Dict[str, str]):
        """
        Run the crew.
        """        
        crew_result = self.crew.kickoff(inputs=inputs)
        
        return crew_result

    def train(self, n_iterations: int, filename: str, inputs: Dict[str, str]):
        """
        Train the crew for a given number of iterations.
        """
        try:
            self.crew.train(n_iterations=n_iterations, filename=filename, inputs=inputs)
        except Exception as e:
            raise Exception(f"An error occurred while training the crew: {e}")

    