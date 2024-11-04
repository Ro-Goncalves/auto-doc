%%{init: {"theme": "base", "themeVariables": { "primaryColor": "#f2f2f2", "primaryTextColor": "#000000", "primaryBorderColor": "#7f7f7f", "lineColor": "#7f7f7f", "tertiaryColor": "#ffffff"}}}%%

```mermaid
flowchart TB
    subgraph Vendas
        direction TB
        subgraph Vendas_Internas
            CAD_Cliente[Cadastro do Cliente]
            DEC_Cliente{Aprovado/Reprovado}
            CONF_Cliente[Confirmação para Cliente]
            INFO_Cliente[Informar Cliente]
        end
        subgraph Vendas_Externas
        end
    end
    
    subgraph Cozinha
        direction TB
        subgraph Preparo
            FAB_Marmita[Fabricação da Marmita]
            DEC_Marmita{Marmitas Conformes/Ajustes Necessários}
        end
        subgraph EmbalaEtiqueta
            EMBALA[Embala e Etiqueta]
        end
    end
    
    subgraph Logística
        direction TB
        subgraph Org_Entregas
            ORG_Entregas[Organização de Entregas]
        end
        subgraph Real_Entregas
            REAL_Entrega[Realização de Entregas]
            DEC_Entrega{Entrega Realizada/Entrega Falha}
            ATUALIZA_Status[Atualiza Status de Entrega]
            NOTIF_Atendimento[Notificar Atendimento]
        end
    end
    
    subgraph Atendimento
        RESOLVE_Problemas[Resolver problemas com entregas]
        FEEDBACK[Receber feedback dos clientes]
    end
    
    subgraph TI
        MANUT_Sistema[Manutenção do Sistema]
    end

    %% Flows for Vendas
    CAD_Cliente -->|Validação| TI
    TI --> DEC_Cliente
    DEC_Cliente -->|Aprovado| CONF_Cliente
    DEC_Cliente -->|Reprovado| INFO_Cliente
    CAD_Cliente --> CAD_Pedido
    CAD_Pedido -->|Validação| TI
    TI --> DEC_Pedido{Aprovado e Pagamento Confirmado / Problema com Pagamento}
    DEC_Pedido -->|Aprovado e Pagamento Confirmado| FAB_Marmita
    DEC_Pedido -->|Problema com Pagamento ou Falta de Ingredientes| INFO_Cliente

    %% Flows for Cozinha
    FAB_Marmita --> EMBALA
    DEC_Marmita -->|Conformes| ORG_Entregas
    DEC_Marmita -->|Ajustes Necessários| FAB_Marmita

    %% Flows for Logística
    ORG_Entregas --> REAL_Entrega
    DEC_Entrega -->|Realizada| ATUALIZA_Status
    DEC_Entrega -->|Falha| NOTIF_Atendimento

    %% Flows for Atendimento
    NOTIF_Atendimento --> RESOLVE_Problemas
    FEEDBACK --> RESOLVE_Problemas
```