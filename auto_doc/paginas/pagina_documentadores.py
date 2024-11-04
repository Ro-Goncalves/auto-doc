import streamlit as st
from datetime import datetime
    
st.info("Documentadores: Automatize sua documentação e ganhe tempo para o que realmente importa! ⏳📄")    

if st.session_state.mostrar_inputs:
    
    example_options = ["Escreva seu próprio Requisito"] + [example['titulo'] for example in st.session_state.exemplos['exemplos']]
    selected_example = st.selectbox("Escolha um exemplo ou escreva seu próprio texto", options=example_options)
    
    if selected_example == "Escreva seu próprio Requisito":
        st.session_state.texto_base = st.text_area(label="Digite ou cole seu Requisito aqui", height=200, key="input_text")
    else:
        selected_text = next(example['texto'] for example in st.session_state.exemplos['exemplos'] if example['titulo'] == selected_example)
        st.session_state.texto_base = st.text_area(label="Digite ou cole seu Requisito aqui", value=selected_text, height=200, key="input_text")
    
    if st.button("Trabalhar", type="primary"):
        with st.spinner("Processando..."):
            crew_result = st.session_state.equipe.run_documentadores({
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
    texto_processado = st.session_state.texto_processado

    st.markdown(texto_processado)
    
    if st.session_state.texto_processado:
        st.download_button(
            label="Baixar Resultado",
            icon="🪄",
            data=st.session_state.texto_processado,
            file_name=f"roteiro_gerado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/plain"
        ) 