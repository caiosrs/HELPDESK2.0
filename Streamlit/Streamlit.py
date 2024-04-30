import streamlit as st
import pandas as pd
import os

# Verificar se o arquivo CSV existe, se não, criar um novo DataFrame vazio
if not os.path.exists('chamados.csv'):
    pd.DataFrame(columns=['ID', 'Assunto', 'Descrição', 'Status']).to_csv('chamados.csv', index=False)

# Função para adicionar um novo chamado
def adicionar_chamado(assunto, descricao):
    chamados = pd.read_csv('chamados.csv')  # Lendo os chamados existentes
    novo_id = f'{len(chamados) + 1:04}'  # Formatar o ID com zeros à esquerda
    novo_chamado = {'ID': novo_id, 'Assunto': assunto, 'Descrição': descricao, 'Status': 'Aberto'}
    chamados = pd.concat([chamados, pd.DataFrame([novo_chamado])], ignore_index=True)
    chamados.to_csv('chamados.csv', index=False)  # Escrevendo os chamados de volta no arquivo

# Função para exibir os chamados existentes
def exibir_chamados():
    chamados = pd.read_csv('chamados.csv')
    st.subheader('Chamados Abertos')
    st.table(chamados)

# Página principal
st.title('Sistema de Chamados')

# Formulário para adicionar um novo chamado
st.subheader('Abrir Novo Chamado')
assunto = st.text_input('Assunto do Chamado')
descricao = st.text_area('Descrição do Chamado')
if st.button('Abrir Chamado'):
    adicionar_chamado(assunto, descricao)
    st.success('Chamado aberto com sucesso!')

exibir_chamados()