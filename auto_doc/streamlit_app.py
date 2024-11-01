import streamlit as st
import yaml
from datetime import datetime
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

def main():     
    st.sidebar.info("Auto Doc: Automatize sua documentação e ganhe tempo para o que realmente importa! 🚀📄")    
    
    if st.session_state.mostrar_inputs:
        st.subheader("Entradas da Equipe")        
       
        example_options = ["Escreva seu próprio Requisito"] + [example['titulo'] for example in st.session_state.exemplos['exemplos']]
        selected_example = st.selectbox("Escolha um exemplo ou escreva seu próprio texto", options=example_options)
        
        if selected_example == "Escreva seu próprio Requisito":
            st.session_state.texto_base = st.text_area(label="Digite ou cole seu Requisito aqui", height=200, key="input_text")
        else:
            selected_text = next(example['texto'] for example in st.session_state.exemplos['exemplos'] if example['titulo'] == selected_example)
            st.session_state.texto_base = st.text_area(label="Digite ou cole seu Requisito aqui", value=selected_text, height=200, key="input_text")
        
        analise_base = analisar_texto(st.session_state.texto_base)
        st.write(f"Caracteres: {len(st.session_state.texto_base)} | Palavras: {analise_base['num_palavras']}")

        if st.button("Trabalhar", type="primary"):
            with st.spinner("Processando..."):
                crew_result = st.session_state.equipe.run({
                    'requisitos': st.session_state.texto_base,
                })
            st.session_state.texto_processado = crew_result.raw           
            st.session_state.saida_tarefas = crew_result.tasks_output            
           
            
            st.session_state.historico.append({
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "texto_base": st.session_state.texto_base,
                "roteiro": crew_result.raw,
                "tasks_output": crew_result.tasks_output,               
            })
            st.session_state.mostrar_inputs = False
            st.rerun() 
    else:
        if st.button("Novo Roteiro", icon="🧪"):
            st.session_state.mostrar_inputs = True
            st.rerun()

    if not st.session_state.mostrar_inputs and st.session_state.saida_tarefas:       
        st.subheader("Resultados das Tarefas")        
       
        task_agent = [task.agent for task in st.session_state.saida_tarefas]
        tabs = st.tabs(task_agent)
        
        for i, tab in enumerate(tabs):
            with tab:
                task = st.session_state.saida_tarefas[i]
                st.write(f"**Resumo:** {task.summary}")
                st.text_area("Resultado", value=task.raw, height=300, key=f"task_output_{i}")

        st.divider()
        
        st.subheader("Resuldado Final")
        texto_processado = st.text_area("Resultado gerado", value=st.session_state.texto_processado, height=300, key="output_text")
        analise_roteiro = analisar_texto(st.session_state.texto_processado)
        st.write(f"Caracteres: {len(texto_processado)} | Palavras: {analise_roteiro['num_palavras']} | Tempo estimado de leitura: {analise_roteiro['tempo_leitura']} minutos")

        if st.session_state.texto_processado:
            st.download_button(
                label="Baixar Resultado",
                icon="🪄",
                data=st.session_state.texto_processado,
                file_name=f"roteiro_gerado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            ) 

auto_doc_page = st.Page(main, title="Central de Comando 🚀", icon=":material/memory:", default=True)

exemplo_resultado_page = st.Page("paginas/exemplo_resultado.py", title="Dossiê de Conquistas 📑💥", icon=":material/text_snippet:")
sobre_equipe_page = st.Page("paginas/sobre_equipe.py", title="Liga dos Documentadores 🦸‍♂️📜", icon=":material/domino_mask:")

pg = st.navigation({
    "Auto Doc": [auto_doc_page],
    "Sobre": [exemplo_resultado_page, sobre_equipe_page],
})


if __name__ == "__main__":
    pg.run()
