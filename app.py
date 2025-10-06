import streamlit as st
#precisa instalar o streamlit
from crud import criar_aluno, listar_alunos, atualizar_alunos, deletar_alunos

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="🐱‍👤")

st.title("Sistema de alunos com postgreSQL")

menu = st.sidebar.radio("menu", ["criar", "listar", "atualizar", "deletar"])

if menu == "criar":
    st.subheader("➕ Criar aluno")
    nome = st.text_input("Nome")
    idade = st.number_input("idade", min_value=14, step=1)
    if st.button("cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.button(f"aluno {nome} foi cadastrado com sucesso!" )
        else:
            st.warning("o campo nome não pode estar vazio")
elif menu == "listar":
    st.subheader("listar_alunos")
    alunos = listar_alunos()
    if alunos:
        st.table(alunos)
    else:
        st.info("nenhum aluno cadastrado")

elif menu == "atualizar":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o aluno", [linha[0] for linha in alunos] )
        nova_idade = st.number_input("Nova idade", min_value=10, step=1)
        if st.button("Atualizar"):
            atualizar_alunos(id_aluno, nova_idade)
            st.success(f"idade do aluno {id_aluno} atualizada com sucesso!")
        else:
            st.info("Nenhum aluno disponivel para atualizar")

elif menu == "deletar":
    st.subheader("Deletar aluno")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("escolha o id para deletar", [linha[0] for linha in alunos])
        if st.button("Deletar"):
            deletar_alunos(id_aluno)
            st.success(f"Aluno do id {id_aluno} deletado com sucesso!")
        else:
            st.info("nenhum aluno disponivel para deletar!")
            