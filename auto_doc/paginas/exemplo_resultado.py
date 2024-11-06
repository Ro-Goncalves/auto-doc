import streamlit as st
import streamlit_mermaid as stmd

st.header("Transforme Alinhamentos em Histórias Épicas com a Força da Inteligência Artificial! 📄✨")
st.divider()

st.markdown("""
    <style>
        .menu-links {
            font-size: 18px;
            font-weight: bold;
            color: #ff5733;  /* Cor personalizada */
            text-decoration: none;  /* Remove underline */
            padding: 10px;
            background-color: #f4f4f4;  /* Fundo da seção */
            border-radius: 5px;
            margin-right: 20px;
        }

        .menu-links:hover {
            background-color: #ff5733;  /* Cor de fundo ao passar o mouse */
            color: white;  /* Cor do texto ao passar o mouse */
        }
    </style>

    <a href="#liga-dos-documentadores" class="menu-links">🔗 Liga dos Documentadores</a>
    <a href="#esquadrao-dos-diagramadores" class="menu-links">🔗 Esquadrão dos Diagramadores</a>
""", unsafe_allow_html=True)

st.markdown("<a name='liga-dos-documentadores'></a>", unsafe_allow_html=True)
st.subheader("Liga dos Documentadores")
st.markdown("""
    🚀 Nossos Documentadores estão a todo vapor! Eles transformaram um alinhamento 
    em um dossiê impecável, pronto para impressionar. Confira o que essa equipe 
    fenomenal conseguiu alcançar! 🌟            
""")

st.markdown("#### Template Utilizado 📐📄")
st.markdown("""
    📋 Estrutura Padrão: O template é o esqueleto do nosso sucesso. Aqui está o 
    modelo estratégico que usamos para organizar cada detalhe.            
""")
with st.expander(label="📝 Um Template Para Guiar", expanded=False, icon=None):
    st.markdown("""
        # Nome do Processo
        Apresentação geral do processo, explicando seu objetivo e contexto dentro 
        da empresa. Detalhe quais problemas ele resolve e quais os benefícios para 
        o time de negócios.

        ## Stakeholders
        Lista dos principais envolvidos no processo, suas responsabilidades e o 
        papel de cada um. Exemplos de stakeholders incluem analistas de negócios, 
        gerentes de projeto, e equipes técnicas.

        ## Atividades
        Descrição detalhada de cada atividade envolvida no processo.

        ### Atividade 1: [Nome da Atividade]
        - **Descrição**: Explicação detalhada do que é feito nesta atividade.
        - **Validações**: Critérios que precisam ser atendidos antes que a atividade 
        seja considerada completa.
        - **Fluxo**: Descrição do passo a passo para realizar a atividade, destacando 
        as interações com outros processos ou sistemas.

        ## Integrações
        Detalhe sobre como o processo se integra com outros sistemas e plataformas, 
        explicando a função de cada integração e sua importância para o sucesso do 
        processo.

        ### Integração 1: [Nome da Integração]
        - **Descrição**: Explicação de como a integração funciona, quais sistemas 
        estão envolvidos e seu papel no processo.

        ## Glossário
        Lista de termos técnicos e seus significados, para garantir que todos os             
    """)

st.markdown("#### Entrada 📝🔍")
st.markdown("""
    🔍 Ponto de Partida: Veja as informações iniciais recebidas pela equipe. Cada 
    detalhe importa para garantir uma documentação precisa.          
""")
with st.expander(label="🔄 E Suas Entradas Transformar", expanded=False, icon=None):
    st.markdown("""
        Anotações da Reunião de Alinhamento - Processo de Vendas de Marmita

        Data: 09/10/2024
        Participantes: Equipe de Vendas, Cozinha, Logística, TI

        Etapa 1: Cadastro do Cliente      
        Info a coletar: nome, CPF/CNPJ (pra empresa tbm), telefone, endereço de 
        entrega (CEP, rua, número, complemento, bairro), e-mail.
        Validações:
        Ver se CPF/CNPJ já existe no sistema.
        Endereço tem que ser válido (e dentro da área de entrega).
        Depois do cadastro, mandar e-mail de confirmação.
        Automação:
        Sistema sugere endereço a partir do CEP.
        E-mail automático pro cliente depois de se cadastrar.
        Roteamento:
        Cadastro OK → vai pro próximo passo (pedido).
        Cadastro não OK (ex: endereço fora da área) → atendente avisa o cliente.
        
        Etapa 2: Cadastro do Pedido
        Info a coletar: tipo de marmita (fitness, vegetariana, tradicional), tamanho (P/M/G), data/hora de 
        entrega, quantidade, observações (ex: restrições alimentares).
        Validações:
        Checar disponibilidade de ingredientes pro que pediram.
        Ver se dá pra produzir na data e quantidade que pediram.
        Checar se pagamento foi feito (online, cartão).
        Automação:
        Integra com sistema de pagamento pra confirmar.
        Confirmação automática pro cliente com os detalhes da entrega.
        Roteamento:
        Pedido OK + pagamento OK → vai pra cozinha.
        Problema com pagamento ou falta de ingredientes → avisa o cliente pra ajustar.
        
        Etapa 3: Fabricação da Marmita
        Cozinha consulta pedidos confirmados no sistema.
        Preparo conforme tipo e restrições alimentares.
        Conferir qualidade dos ingredientes antes de usar.
        Embalar de forma correta pra manter segurança alimentar.
        Validações:
        Conferir se todas as marmitas estão como o cliente pediu.
        Etiquetar tudo certinho com nome do cliente, tipo, data de preparo.
        Automação:
        Sistema gera lista diária de produção.
        Registro automático das marmitas prontas pro próximo passo (entrega).
        Roteamento:
        Marmitas OK → vai pra entrega.
        Ajuste necessário → notificar cozinha.
        
        Etapa 4: Entrega
        Entregador verifica a lista do dia e endereços.
        Organizar as marmitas por rota.
        Registrar no sistema quando entregar (hora, assinatura do cliente).
        Validações:
        Ver se todas as marmitas estão na rota certa.
        Confirmar com o cliente e pegar assinatura/foto.
        Status: entregue, tentativa de entrega, não entregue.
        Automação:
        Roteirização automática (otimizar rotas).
        Notificar cliente por SMS ou app (status da entrega).
        Roteamento:
        Entrega OK → processo encerrado.
        Entrega falhou (cliente ausente, endereço errado) → notificar atendimento.
        
        Obs.:

        Verificar com a TI se a integração com o sistema de pagamento está estável.
        Cozinha pediu atenção na descrição dos pedidos com restrição alimentar.
        Logística sugeriu revisar a área de entrega, aumentar cobertura.            
    """)
    
st.markdown("#### Resultado Final 🏆📜")
st.markdown("""
    🏆 Conquista Completa: O trabalho finalizado é um documento coeso e poderoso. 
    Confira o resultado do esforço dos Documentadores!
""")
with st.expander(label="❤️ Em um Resultado Para Amar", expanded=False, icon=None):
    st.markdown("""
        # Processo de Vendas de Marmita

        ## Apresentação

        O processo de vendas de marmita tem como objetivo atender à demanda por refeições saborosas e práticas, oferecendo aos clientes uma variedade de opções de marmitas (fitness, vegetariana, tradicional) com diferentes tamanhos (P/M/G). O processo garante a qualidade e segurança alimentar, desde o cadastro do cliente até a entrega da marmita. Ele contribui para a otimização do tempo e recursos da empresa, além de proporcionar uma experiência positiva para o cliente.

        ## Stakeholders

        | Stakeholder | Responsabilidades | Papel no Processo |
        |---|---|---|
        | Equipe de Vendas | Cadastrar clientes, receber pedidos, validar pagamentos, comunicar o status do pedido ao cliente. | Ponto de contato inicial com o cliente, responsável por garantir a qualidade da informação coletada. |
        | Cozinha | Preparar as marmitas conforme o pedido, garantir a qualidade dos ingredientes e a segurança alimentar, embalar as marmitas. | Responsável pela produção das marmitas, garantindo a qualidade e a conformidade com os pedidos. |
        | Logística | Organizar as entregas, realizar a entrega das marmitas, registrar a entrega no sistema. | Responsável por garantir a entrega das marmitas aos clientes no prazo e local correto. |
        | TI | Manter a integração do sistema de pagamento, garantir a estabilidade do sistema. | Responsável pela infraestrutura tecnológica e pela integração dos sistemas utilizados no processo. |
        | Atendimento | Resolver problemas com entregas, receber feedback dos clientes. | Responsável por lidar com as demandas dos clientes, como problemas com entregas ou solicitações de informações. |

        ## Atividades

        ### 1. Cadastro do Cliente

        - **Descrição**: Nesta atividade, a Equipe de Vendas coleta informações do cliente para criar um cadastro no sistema. As informações coletadas incluem nome, CPF/CNPJ, telefone, endereço de entrega (CEP, rua, número, complemento, bairro) e e-mail.
        - **Validações**:
            - **CPF/CNPJ**: o sistema valida o CPF/CNPJ do cliente para garantir que seja válido e esteja dentro da base de dados.
            - **Endereço de entrega**: o sistema valida o endereço de entrega para verificar se está dentro da área de cobertura da entrega.
        - **Fluxo**:
            1. O cliente entra em contato com a Equipe de Vendas para realizar o cadastro.
            2. A Equipe de Vendas coleta as informações do cliente.
            3. O sistema valida o CPF/CNPJ e o endereço de entrega.
            4. **Se o cadastro for aprovado, o sistema envia um e-mail de confirmação ao cliente.**
            5. **Se o cadastro for reprovado, a Equipe de Vendas informa o cliente sobre a reprovação (ex: endereço fora da área de entrega).**

        ### 2. Cadastro do Pedido

        - **Descrição**: Nesta atividade, a Equipe de Vendas recebe o pedido do cliente, coletando informações como tipo de marmita (fitness, vegetariana, tradicional), tamanho (P/M/G), data/hora de entrega, quantidade e observações (ex: restrições alimentares).
        - **Validações**:
            - **Disponibilidade de ingredientes**: o sistema verifica se os ingredientes necessários para a marmita estão disponíveis.
            - **Capacidade de produção**: o sistema verifica se a Cozinha tem capacidade de produzir a quantidade de marmitas solicitadas na data e hora desejadas.
            - **Pagamento**: o sistema valida o pagamento online ou por cartão.
        - **Fluxo**:
            1. O cliente entra em contato com a Equipe de Vendas para realizar o pedido.
            2. A Equipe de Vendas coleta as informações do pedido.
            3. O sistema valida a disponibilidade de ingredientes, a capacidade de produção e o pagamento.
            4. **Se o pedido for aprovado e o pagamento confirmado, o sistema encaminha o pedido para a Cozinha.**
            5. **Se houver algum problema com o pagamento ou falta de ingredientes, a Equipe de Vendas informa o cliente para ajustar o pedido.**

        ### 3. Fabricação da Marmita

        - **Descrição**: Nesta atividade, a Cozinha prepara as marmitas de acordo com o pedido do cliente, garantindo a qualidade dos ingredientes e a segurança alimentar.
        - **Validações**:
            - **Conferência das marmitas**: a Cozinha confere se todas as marmitas estão de acordo com o pedido do cliente (tipo, tamanho, restrições alimentares).
            - **Etiquetagem das marmitas**: as marmitas são etiquetadas com o nome do cliente, tipo e data de preparo.
        - **Fluxo**:
            1. A Cozinha consulta os pedidos confirmados no sistema.
            2. A Cozinha prepara as marmitas conforme o pedido do cliente.
            3. A Cozinha confere a qualidade dos ingredientes e a segurança alimentar.
            4. A Cozinha embala as marmitas de forma segura.
            5. **A Cozinha confere se todas as marmitas estão de acordo com o pedido do cliente.**
            6. **A Cozinha etiqueta as marmitas.**
            7. **O sistema registra as marmitas prontas para a etapa de entrega.**
            8. **As marmitas prontas são encaminhadas para a Logística.**
            9. **Se houver algum ajuste necessário, a Cozinha é notificada.**

        ### 4. Entrega

        - **Descrição**: Nesta atividade, a Logística organiza a entrega das marmitas aos clientes, garantindo que as marmitas sejam entregues no prazo e no local correto.
        - **Validações**:
            - **Conferência das marmitas**: a Logística confere se todas as marmitas estão na rota correta.
            - **Confirmação da entrega**: a Logística confirma a entrega com o cliente e obtém a assinatura ou foto do cliente.
            - **Status da entrega**: a Logística define o status da entrega: entregue, tentativa de entrega, não entregue.
        - **Fluxo**:
            1. A Logística verifica a lista de entregas do dia e os endereços.
            2. A Logística organiza as marmitas por rota.
            3. A Logística realiza a entrega das marmitas.
            4. **A Logística registra no sistema a hora da entrega e a assinatura do cliente.**
            5. **A Logística define o status da entrega.**
            6. **Se a entrega for realizada, o processo é concluído.**
            7. **Se a entrega falhar (cliente ausente, endereço errado), a Logística notifica o Atendimento.**

        ## Integrações

        ### Integração com Sistema de Pagamento

        - **Descrição**: O sistema de vendas se integra com o sistema de pagamento para validar o pagamento online ou por cartão. Essa integração garante que o pagamento seja processado com segurança e que o pedido seja aprovado somente após a confirmação do pagamento.
        - **Função**: Validar o pagamento e garantir a segurança da transação.
        - **Importância**: Permite que o cliente realize o pagamento de forma rápida e segura, agilizando o processo de venda.

        ## Glossário

        - **CPF/CNPJ**: Número de Identificação do Contribuinte (CPF) para pessoas físicas e Cadastro Nacional de Pessoa Jurídica (CNPJ) para pessoas jurídicas.
        - **Restrições Alimentares**: Indicações de alimentos que o cliente não pode consumir, como glúten, lactose, etc.
        - **Status da Entrega**: Indica se a entrega foi realizada, se houve tentativa de entrega ou se a entrega não foi realizada.

        ## Considerações Especiais

        - **Integração com sistema de pagamento**: É importante verificar com a TI a estabilidade da integração para garantir que o sistema de pagamento funcione corretamente.
        - **Restrições alimentares**: A Cozinha solicita atenção na descrição dos pedidos com restrições alimentares para garantir que as marmitas sejam preparadas de acordo com as necessidades do cliente.
        - **Área de entrega**: A Logística sugere revisar a área de entrega e aumentar a cobertura para atender a um maior número de clientes.

        ## Observações

        - Este documento é uma versão inicial e pode ser atualizado conforme necessário.
        - A documentação técnica completa será elaborada pelo Agente de Documentação Técnica com base nas informações aqui descritas.

        ## Próximos Passos

        - Reunião com a equipe para discutir e validar as informações.
        - Elaboração da documentação técnica completa.

        ## Responsável pela Documentação

        Analista de Processos            
    """)
    
st.divider()

st.markdown("<a name='esquadrao-dos-diagramadores'></a>", unsafe_allow_html=True)
st.subheader("Esquadrão dos Diagramadores")
st.markdown("""
    ✨ Nosso Esquadrão dos Diagramadores está pronto para ação! Com uma visão estratégica 
    e olhos afiados para detalhes, eles pegaram um processo complexo e o transformaram em 
    um diagrama que até o caos entenderia! Confira o que essa equipe incrível entregou! 🚀📊            
""")

st.markdown("#### Entrada 📥🛠️")
st.markdown("""
    🔍 Ponto de Partida: Conheça os dados iniciais com que nossa equipe trabalhou. Cada 
    setor, cada atividade — tudo cuidadosamente mapeado para criar um fluxo poderoso!
""")
with st.expander(label="🔍 Mergulhar nas Entradas para Desvendar o Fluxo!", expanded=False, icon=None):
    st.markdown("""
        # Processo de Vendas de Marmita

        ## Apresentação

        O processo de vendas de marmita tem como objetivo atender à demanda por refeições saborosas e práticas, oferecendo aos clientes uma variedade de opções de marmitas (fitness, vegetariana, tradicional) com diferentes tamanhos (P/M/G). O processo garante a qualidade e segurança alimentar, desde o cadastro do cliente até a entrega da marmita. Ele contribui para a otimização do tempo e recursos da empresa, além de proporcionar uma experiência positiva para o cliente.

        ## Stakeholders

        | Stakeholder | Responsabilidades | Papel no Processo |
        |---|---|---|
        | Equipe de Vendas | Cadastrar clientes, receber pedidos, validar pagamentos, comunicar o status do pedido ao cliente. | Ponto de contato inicial com o cliente, responsável por garantir a qualidade da informação coletada. |
        | Cozinha | Preparar as marmitas conforme o pedido, garantir a qualidade dos ingredientes e a segurança alimentar, embalar as marmitas. | Responsável pela produção das marmitas, garantindo a qualidade e a conformidade com os pedidos. |
        | Logística | Organizar as entregas, realizar a entrega das marmitas, registrar a entrega no sistema. | Responsável por garantir a entrega das marmitas aos clientes no prazo e local correto. |
        | TI | Manter a integração do sistema de pagamento, garantir a estabilidade do sistema. | Responsável pela infraestrutura tecnológica e pela integração dos sistemas utilizados no processo. |
        | Atendimento | Resolver problemas com entregas, receber feedback dos clientes. | Responsável por lidar com as demandas dos clientes, como problemas com entregas ou solicitações de informações. |

        ## Atividades

        ### 1. Cadastro do Cliente

        - **Descrição**: Nesta atividade, a Equipe de Vendas coleta informações do cliente para criar um cadastro no sistema. As informações coletadas incluem nome, CPF/CNPJ, telefone, endereço de entrega (CEP, rua, número, complemento, bairro) e e-mail.
        - **Validações**:
            - **CPF/CNPJ**: o sistema valida o CPF/CNPJ do cliente para garantir que seja válido e esteja dentro da base de dados.
            - **Endereço de entrega**: o sistema valida o endereço de entrega para verificar se está dentro da área de cobertura da entrega.
        - **Fluxo**:
            1. O cliente entra em contato com a Equipe de Vendas para realizar o cadastro.
            2. A Equipe de Vendas coleta as informações do cliente.
            3. O sistema valida o CPF/CNPJ e o endereço de entrega.
            4. **Se o cadastro for aprovado, o sistema envia um e-mail de confirmação ao cliente.**
            5. **Se o cadastro for reprovado, a Equipe de Vendas informa o cliente sobre a reprovação (ex: endereço fora da área de entrega).**

        ### 2. Cadastro do Pedido

        - **Descrição**: Nesta atividade, a Equipe de Vendas recebe o pedido do cliente, coletando informações como tipo de marmita (fitness, vegetariana, tradicional), tamanho (P/M/G), data/hora de entrega, quantidade e observações (ex: restrições alimentares).
        - **Validações**:
            - **Disponibilidade de ingredientes**: o sistema verifica se os ingredientes necessários para a marmita estão disponíveis.
            - **Capacidade de produção**: o sistema verifica se a Cozinha tem capacidade de produzir a quantidade de marmitas solicitadas na data e hora desejadas.
            - **Pagamento**: o sistema valida o pagamento online ou por cartão.
        - **Fluxo**:
            1. O cliente entra em contato com a Equipe de Vendas para realizar o pedido.
            2. A Equipe de Vendas coleta as informações do pedido.
            3. O sistema valida a disponibilidade de ingredientes, a capacidade de produção e o pagamento.
            4. **Se o pedido for aprovado e o pagamento confirmado, o sistema encaminha o pedido para a Cozinha.**
            5. **Se houver algum problema com o pagamento ou falta de ingredientes, a Equipe de Vendas informa o cliente para ajustar o pedido.**

        ### 3. Fabricação da Marmita

        - **Descrição**: Nesta atividade, a Cozinha prepara as marmitas de acordo com o pedido do cliente, garantindo a qualidade dos ingredientes e a segurança alimentar.
        - **Validações**:
            - **Conferência das marmitas**: a Cozinha confere se todas as marmitas estão de acordo com o pedido do cliente (tipo, tamanho, restrições alimentares).
            - **Etiquetagem das marmitas**: as marmitas são etiquetadas com o nome do cliente, tipo e data de preparo.
        - **Fluxo**:
            1. A Cozinha consulta os pedidos confirmados no sistema.
            2. A Cozinha prepara as marmitas conforme o pedido do cliente.
            3. A Cozinha confere a qualidade dos ingredientes e a segurança alimentar.
            4. A Cozinha embala as marmitas de forma segura.
            5. **A Cozinha confere se todas as marmitas estão de acordo com o pedido do cliente.**
            6. **A Cozinha etiqueta as marmitas.**
            7. **O sistema registra as marmitas prontas para a etapa de entrega.**
            8. **As marmitas prontas são encaminhadas para a Logística.**
            9. **Se houver algum ajuste necessário, a Cozinha é notificada.**

        ### 4. Entrega

        - **Descrição**: Nesta atividade, a Logística organiza a entrega das marmitas aos clientes, garantindo que as marmitas sejam entregues no prazo e no local correto.
        - **Validações**:
            - **Conferência das marmitas**: a Logística confere se todas as marmitas estão na rota correta.
            - **Confirmação da entrega**: a Logística confirma a entrega com o cliente e obtém a assinatura ou foto do cliente.
            - **Status da entrega**: a Logística define o status da entrega: entregue, tentativa de entrega, não entregue.
        - **Fluxo**:
            1. A Logística verifica a lista de entregas do dia e os endereços.
            2. A Logística organiza as marmitas por rota.
            3. A Logística realiza a entrega das marmitas.
            4. **A Logística registra no sistema a hora da entrega e a assinatura do cliente.**
            5. **A Logística define o status da entrega.**
            6. **Se a entrega for realizada, o processo é concluído.**
            7. **Se a entrega falhar (cliente ausente, endereço errado), a Logística notifica o Atendimento.**

        ## Integrações

        ### Integração com Sistema de Pagamento

        - **Descrição**: O sistema de vendas se integra com o sistema de pagamento para validar o pagamento online ou por cartão. Essa integração garante que o pagamento seja processado com segurança e que o pedido seja aprovado somente após a confirmação do pagamento.
        - **Função**: Validar o pagamento e garantir a segurança da transação.
        - **Importância**: Permite que o cliente realize o pagamento de forma rápida e segura, agilizando o processo de venda.

        ## Glossário

        - **CPF/CNPJ**: Número de Identificação do Contribuinte (CPF) para pessoas físicas e Cadastro Nacional de Pessoa Jurídica (CNPJ) para pessoas jurídicas.
        - **Restrições Alimentares**: Indicações de alimentos que o cliente não pode consumir, como glúten, lactose, etc.
        - **Status da Entrega**: Indica se a entrega foi realizada, se houve tentativa de entrega ou se a entrega não foi realizada.

        ## Considerações Especiais

        - **Integração com sistema de pagamento**: É importante verificar com a TI a estabilidade da integração para garantir que o sistema de pagamento funcione corretamente.
        - **Restrições alimentares**: A Cozinha solicita atenção na descrição dos pedidos com restrições alimentares para garantir que as marmitas sejam preparadas de acordo com as necessidades do cliente.
        - **Área de entrega**: A Logística sugere revisar a área de entrega e aumentar a cobertura para atender a um maior número de clientes.

        ## Observações

        - Este documento é uma versão inicial e pode ser atualizado conforme necessário.
        - A documentação técnica completa será elaborada pelo Agente de Documentação Técnica com base nas informações aqui descritas.

        ## Próximos Passos

        - Reunião com a equipe para discutir e validar as informações.
        - Elaboração da documentação técnica completa.

        ## Responsável pela Documentação

        Analista de Processos            
    """)
  
st.markdown("#### Resultado Final 🏅💼")
st.markdown("""
    🎉 Diagrama Desenhado e Validado: O produto final é um mapa visual impecável! Veja como 
    o Esquadrão dos Diagramadores transformou informações em uma obra-prima de clareza e 
    eficiência.
""")
with st.expander(label="✨ Transformar em Diagrama com Maestria!", expanded=False, icon=None):
    code = """
graph TD
    subgraph Equipe de Vendas
        A[Cadastro do Cliente] --> B{CPF/CNPJ e Endereço Válidos?}
        B -- Sim --> C[Cadastro do Pedido]
        B -- Não --> F[Informar Reprovação de Cadastro]
        C --> D{Ingredientes, Produção e Pagamento OK?}
        D -- Sim --> E[Informar Pedido à Cozinha]
        D -- Não --> G[Informar Reprovação de Pedido]
    end
    
    subgraph Cozinha
        E --> H[Preparar Marmitas]
        H --> I[Conferir e Etiquetar Marmitas]
        I --> J[Registrar Marmitas Prontas no Sistema]
        J --> K[Encaminhar para Logística]
    end

    subgraph Logística
        K --> L[Organizar Entregas por Rota]
        L --> M[Realizar Entrega]
        M --> N{Entrega Realizada?}
        N -- Sim --> O[Registrar Entrega no Sistema]
        N -- Não --> P[Notificar Atendimento]
    end

    subgraph Atendimento
        P --> Q[Solucionar Problema de Entrega]
        Q --> R[Informar Resultado ao Cliente]
    end

    F --> Z[Fim do Processo]
    G --> Z
    O --> Z
    R --> Z


    style F fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#f9f,stroke:#333,stroke-width:2px
    style O fill:#ccf,stroke:#333,stroke-width:2px
    style Z fill:#ccf,stroke:#333,stroke-width:2px
"""
    stmd.st_mermaid(code,  height="500px")
    st.markdown("""
        ## Relatório de Conformidade do Diagrama de Processos de Vendas de Marmita

        **Conformidade Geral:** O diagrama revisado está mais alinhado aos requisitos descritos no documento, com maior detalhamento das atividades e fluxos. A divisão por setores (Equipe de Vendas, Cozinha, Logística e Atendimento) está clara e facilita a compreensão das responsabilidades.

        **Melhorias Implementadas:**

        * **Etapa de Cadastro do Cliente:** Foi desmembrada em etapas mais granulares, incluindo a coleta de dados, validação e criação do cadastro.
        * **Etapa de Cadastro do Pedido:** Foi integrada à etapa de vendas e inclui a validação do pedido e o processamento do pagamento.
        * **Etapa de Fabricação da Marmita:** Foi simplificada, mantendo o foco nas atividades principais da cozinha.
        * **Etapa de Entrega:** Foi detalhada para incluir o registro da entrega no sistema.
        * **Etapa de Atendimento:** Foi incluída para representar o tratamento de problemas na entrega.
        * **Fluxos de Reprovação/Ajuste:** Os fluxos de reprovação de cadastro, pedido e pagamento, assim como de ajuste de pedido, foram adicionados para representar os cenários alternativos.
        * **Nomenclatura:** As atividades foram renomeadas para melhor refletir as ações realizadas.
        * **Remoção de nós desnecessários:** Nós como "Aprovado?" foram substituídos por fluxos mais descritivos com o uso de "Sim" e "Não" nas setas.

        **Sugestões de Ajustes:**

        * **Integração com Sistemas:** Embora não representado visualmente no diagrama, é importante documentar a integração com o sistema de pagamento e outros sistemas relevantes.  Recomenda-se adicionar uma nota ao diagrama mencionando essas integrações.
        * **Métricas:**  Para acompanhamento e melhoria contínua do processo, sugere-se definir métricas relevantes, como tempo médio de entrega, taxa de sucesso de entregas, etc.  Essas métricas podem ser adicionadas como informações complementares ao diagrama.

        **Validação Final:** O diagrama revisado atende aos requisitos especificados e representa o fluxo do processo de vendas de marmita de forma clara e completa.  As melhorias implementadas garantem maior precisão e facilitam a compreensão do processo pelos stakeholders.  Com a implementação das sugestões, o diagrama se tornará ainda mais robusto e útil para a gestão do processo.          
    """)
  
  