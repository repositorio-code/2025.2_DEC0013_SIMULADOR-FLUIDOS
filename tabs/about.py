import streamlit as st

def render_about_tab():
    """Renderiza a aba Sobre"""
    st.header("Sobre a Aplicação")
    
    st.markdown("""
    ### 📋 Descrição
    Esta aplicação realiza simulações completas de escoamento em sistemas de tubulações e canais abertos.
    
    ### 🎯 Funcionalidades
    
    #### Configuração de Fluidos
    - Seleção de fluidos pré-configurados: Água, Ar, Óleo leve, Gás ideal ou Personalizado
    - Ajuste de temperatura de operação (-50°C a 500°C)
    - Configuração de pressão inicial do sistema
    - Entrada por vazão ou velocidade
    - Cálculo automático de propriedades termofísicas
    
    #### Sistema de Tubulações em Série
    - **Múltiplos trechos**: Adicione quantos trechos precisar
    - **Materiais variados**: PVC, Cobre, Aço comercial, Aço galvanizado, Concreto, Ferro fundido
    - **Variação de diâmetro** entre trechos
    - **Desnível**: Configure elevações positivas ou negativas
    - **Acessórios completos**:
      - Contrações e expansões
      - Curvas de 90°
      - Válvulas (gaveta, globo, esfera, retenção)
      - Tês (passagem direta e lateral)
    - **Perfil de pressão**: Visualize a pressão ao longo de todo o sistema
    - **Alertas de velocidade**: Verificação automática de faixas recomendadas
    
    #### Análise de Canais Abertos
    - Cálculo de profundidade normal e crítica
    - Número de Froude e classificação de regime
    - Geometria hidráulica completa
    
    #### Simulações Avançadas
    - Variação de vazão: Análise de perda de carga e velocidade
    - Variação de pressão de entrada
    - Comparação entre materiais
    - Gráficos interativos e exportáveis
    
    ### 📊 Métodos de Cálculo
    
    #### Escoamento em Tubos
    
    **Número de Reynolds:**
    ```
    Re = (ρ × V × D) / μ
    ```
    
    **Fator de Atrito (Colebrook-White):**
    ```
    1/√f = -2 × log₁₀[(ε/D)/3.7 + 2.51/(Re×√f)]
    ```
    
    **Perda de Carga Distribuída (Darcy-Weisbach):**
    ```
    hf = f × (L/D) × (V²/2g)
    ```
    
    **Perdas Localizadas:**
    ```
    hL = K × (V²/2g)
    ```
    
    **Coeficientes K:**
    - Contração: K = 0.5 × (1 - β²)
    - Expansão: K = (1 - β²)²
    - Curva 90°: K = 0.3
    - Válvula gaveta: K = 0.15
    - Válvula globo: K = 10.0
    - Válvula esfera: K = 0.05
    - Válvula retenção: K = 2.5
    - Tê passagem: K = 0.6
    - Tê lateral: K = 1.8
    
    **Altura Manométrica Total:**
    ```
    H = hf + ΣhL + Δz
    ```
    
    **Variação de Pressão:**
    ```
    ΔP = H × ρ × g
    ```
    
    #### Velocidades Recomendadas
    
    **Água:**
    - Mínima: 0,5 m/s (evita sedimentação)
    - Máxima: 3,0 m/s (evita erosão e ruído)
    - Sucção de bombas: 0,6 a 1,5 m/s
    - Recalque: 1,5 a 2,5 m/s
    
    **Ar:**
    - Máxima: 15 m/s
    
    ### 🛠️ Tecnologias
    - **Streamlit**: Interface web interativa
    - **Fluids**: Biblioteca de engenharia de fluidos
    - **Plotly**: Visualizações gráficas profissionais
    - **Pandas/NumPy**: Processamento de dados
    
    ### 💡 Dicas de Uso
    
    1. **Sistema em série**: Adicione trechos para modelar seu sistema completo
    2. **Pressão variável**: Observe como a pressão diminui ao longo do sistema
    3. **Otimização**: Use as simulações para encontrar o melhor diâmetro ou material
    4. **Acessórios**: Não esqueça de incluir válvulas e curvas para cálculo preciso
    5. **Velocidade**: Sempre verifique os alertas de velocidade
    """)
    
    st.info("""
    **💡 Dica:** Use a sidebar para configurar o fluido e condições iniciais. 
    Adicione múltiplos trechos para modelar sistemas complexos e observe o perfil de pressão!
    """)
