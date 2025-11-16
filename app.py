import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
import yaml

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.7)

template = '''
Você é um pedagogo experiente e especialista em planejamento educacional.
Crie um plano de aula detalhado sobre o tema "{tema}" para alunos do nível "{nivel_ensino}".

O plano deve ter duração de {duracao} e seguir a metodologia "{metodologia}".

Estruture o plano de aula com os seguintes elementos:
- Objetivos de aprendizagem
- Conteúdo programático
- Metodologia e atividades práticas
- Recursos necessários
- Avaliação
- {elemento_extra}

Formate o plano de aula utilizando Markdown com seções bem definidas.
Seja criativo e prático nas sugestões de atividades.
'''

prompt_template = PromptTemplate.from_template(template=template)

# Opções de configuração
temas = [
    'Fotossíntese e Ecossistemas',
    'Revolução Industrial',
    'Equações do Segundo Grau',
    'Interpretação de Textos Literários',
    'Programação em Python',
    'Sistema Solar e Astronomia',
    'Verbos e Tempos Verbais',
    'Geometria Espacial'
]

niveis_ensino = [
    'Ensino Fundamental I (1º ao 5º ano)',
    'Ensino Fundamental II (6º ao 9º ano)',
    'Ensino Médio',
    'Educação de Jovens e Adultos (EJA)',
    'Ensino Técnico'
]

duracoes = ['50 minutos', '1h30min', '2 horas', '3 horas']

metodologias = [
    'Aprendizagem Baseada em Projetos',
    'Sala de Aula Invertida',
    'Gamificação',
    'Aprendizagem Colaborativa',
    'Ensino Tradicional com Práticas Inovadoras'
]

elementos_extras = [
    'Sugestões de adaptações para alunos com necessidades especiais',
    'Atividades de extensão para casa',
    'Integração com tecnologias digitais',
    'Conexões interdisciplinares',
    'Estratégias de engajamento para alunos desmotivados'
]

# Interface Streamlit
st.title('🎓 Gerador de Planos de Aula com IA')
st.markdown('*Crie planos de aula personalizados em segundos!*')

# Sidebar com configurações
st.sidebar.header('⚙️ Configurações do Plano de Aula')

tema = st.sidebar.selectbox('📚 Tema da aula:', temas)
nivel_ensino = st.sidebar.selectbox('👥 Nível de ensino:', niveis_ensino)
duracao = st.sidebar.selectbox('⏱️ Duração da aula:', duracoes)
metodologia = st.sidebar.selectbox('🎯 Metodologia:', metodologias)
elemento_extra = st.sidebar.selectbox('✨ Elemento adicional:', elementos_extras)

st.sidebar.markdown('---')

if st.sidebar.button('🚀 Gerar Plano de Aula', type='primary'):
    with st.spinner('Gerando seu plano de aula personalizado...'):
        prompt = prompt_template.format(
            tema=tema,
            nivel_ensino=nivel_ensino,
            duracao=duracao,
            metodologia=metodologia,
            elemento_extra=elemento_extra
        )

        response = openai.invoke(prompt)

        st.success('✅ Plano de aula gerado com sucesso!')
        st.markdown('---')
        st.markdown(response.content)
        
        # Botão para download
        st.download_button(
            label='📥 Baixar Plano de Aula',
            data=response.content,
            file_name=f'plano_aula_{tema.replace(" ", "_")}.md',
            mime='text/markdown'
        )
else:
    st.info('👈 Configure os parâmetros na barra lateral e clique em "Gerar Plano de Aula"')
    
    # Exemplo visual
    st.markdown('### 📋 Exemplo de uso:')
    st.markdown('''
    1. Selecione o **tema** da sua aula
    2. Escolha o **nível de ensino** dos alunos
    3. Defina a **duração** da aula
    4. Selecione a **metodologia** pedagógica
    5. Adicione um **elemento extra** ao plano
    6. Clique em **Gerar Plano de Aula**
    ''')