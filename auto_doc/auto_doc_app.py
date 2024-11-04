import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import yaml
from equipe.auto_doc_execucao import AutoDocController as EquipeController

st.set_page_config(layout="wide", page_title="Auto Doc", page_icon="🤖")
st.title("🤖📄✨ Auto Doc")


def status_inicial():
    if 'texto_base' not in st.session_state:
        st.session_state.texto_base = ""  
    if 'texto_processado' not in st.session_state:
        st.session_state.texto_processado = ""
    if 'mostrar_inputs' not in st.session_state:
        st.session_state.mostrar_inputs = True
    if 'saida_tarefas' not in st.session_state:
        st.session_state.saida_tarefas = []
    if 'historico' not in st.session_state:
        st.session_state.historico = []
    if 'exemplos' not in st.session_state:
        st.session_state.exemplos = []

status_inicial()

@st.cache_resource
def analisar_texto(texto):
    palavras = texto.split()
    return {
        "num_palavras": len(palavras),
        "tempo_leitura": len(palavras) // 200  # Assumindo uma velocidade média de leitura de 200 palavras por minuto
    }

@st.cache_resource
def criar_equipe():
    return EquipeController()

st.session_state.equipe = criar_equipe()

@st.cache_data
def carregando_exemplo():
    with open('auto_doc/equipe/config/exemplos.yaml', 'r') as file:
        exemplo = yaml.safe_load(file)
    return exemplo

st.session_state.exemplos = carregando_exemplo()

pagina_documentadores = st.Page("paginas/pagina_documentadores.py", title="Central de Documentação ⚙️", icon=":material/memory:", default=True)
pagina_diagramadores = st.Page("paginas/pagina_diagramadores.py", title="Central de Diagramação ⚙️", icon=":material/memory:")

exemplo_resultado_page = st.Page("paginas/exemplo_resultado.py", title="Dossiê de Conquistas 📑💥", icon=":material/text_snippet:")
sobre_equipe_page = st.Page("paginas/sobre_equipe.py", title="Liga dos Documentadores 🦸‍♂️📜", icon=":material/domino_mask:")

pg = st.navigation({
    "Auto Doc": [pagina_documentadores, pagina_diagramadores],
    "Sobre": [exemplo_resultado_page, sobre_equipe_page],
})


if __name__ == "__main__":
    pg.run()
