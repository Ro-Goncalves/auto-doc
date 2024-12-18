from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import chromadb.utils.embedding_functions as embedding_functions
import os

from pydantic import BaseModel
from typing import List, Optional

class Atividade(BaseModel):
    nome: str
    descricao: str
    validacoes: Optional[List[str]]
    fluxo: str

class Integracao(BaseModel):
    nome: str
    descricao: str

class TemplateProcesso(BaseModel):
    nome_processo: str
    apresentacao: str
    stakeholders: List[str]
    atividades: List[Atividade]
    integracoes: List[Integracao]
    glossario: Optional[dict]
    
@CrewBase
class EquipeDocumentadores():
    @agent
    def analista_processos(self) -> Agent:            
        return Agent(
            config=self.agents_config['analista_processos'],
            llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.25),
            max_rpm=30,
            memory=True,
            allow_delegation=False,
            verbose=True, 
        )
        
    @agent
    def especialista_documentacao(self) -> Agent:             
        return Agent(
            config=self.agents_config['especialista_documentacao'],
            llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.50),
            max_rpm=30,
            memory=True,
            allow_delegation=False,
            verbose=True,
        ) 
        
    @agent
    def auditor_documentacao(self) -> Agent:             
        return Agent(
            config=self.agents_config['auditor_documentacao'],
            llm=LLM(model="gemini/gemini-1.5-flash", temperature=0.75),
            max_rpm=30,
            memory=True,
            allow_delegation=False,
            verbose=True,          
        ) 
    
    @task
    def mapear_processo(self) -> Task:       
        return Task(
            config=self.tasks_config['mapear_processo'],
            agent=self.analista_processos(),
            #output_pydantic=TemplateProcesso
        ) 
        
    @task
    def documentar_processo(self) -> Task: 
        return Task(
            config=self.tasks_config['documentar_processo'],
            agent=self.especialista_documentacao(),
            #output_pydantic=TemplateProcesso
        )
        
    @task
    def auditar_documentacao(self) -> Task: 
        return Task(
            config=self.tasks_config['auditar_documentacao'],
            agent=self.auditor_documentacao(),
            #output_pydantic=TemplateProcesso
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