from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import chromadb.utils.embedding_functions as embedding_functions
import os
    
@CrewBase
class EquipeDiagramadores():
    @agent
    def identificador_atividades(self) -> Agent:            
        return Agent(
            config=self.agents_config['identificador_atividades'],
            llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.25),
            max_rpm=30,
            memory=True,
            allow_delegation=False,
            verbose=True, 
        )
        
    @agent
    def diagramador_processos(self) -> Agent:             
        return Agent(
            config=self.agents_config['diagramador_processos'],
            llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.50),
            max_rpm=30,
            memory=True,
            allow_delegation=False,
            verbose=True,
        ) 
        
    @agent
    def avaliador_conformidade(self) -> Agent:             
        return Agent(
            config=self.agents_config['avaliador_conformidade'],
            llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.75),
            max_rpm=30,
            memory=True,
            allow_delegation=False,
            verbose=True,          
        ) 
    
    @task
    def identificar_atividades(self) -> Task:       
        return Task(
            config=self.tasks_config['identificar_atividades'],
            agent=self.identificador_atividades(),            
        ) 
        
    @task
    def diagramar_processo(self) -> Task: 
        return Task(
            config=self.tasks_config['diagramar_processo'],
            agent=self.diagramador_processos(),            
        )
        
    @task
    def avaliar_conformidade(self) -> Task: 
        return Task(
            config=self.tasks_config['avaliar_conformidade'],
            agent=self.avaliador_conformidade(),            
        )

    @crew
    def crew(self) -> Crew: 
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            cache=True,
            verbose=True,            
            memory=True,
            embedder=embedding_functions.GoogleGenerativeAiEmbeddingFunction(
                api_key=os.getenv("GOOGLE_API_KEY"),
                model_name="models/text-embedding-004"
            )
        )