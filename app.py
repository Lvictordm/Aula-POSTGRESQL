import streamlit as st
#precisa instalar o streamlit
from crud import criar_aluno, listar_alunos, atualizar_alunos, remover_alunos

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
elif menu == "lisar":
    st.subheader("listar_alunos")
    alunos = listar_alunos()
    if alunos:
        st.table(alunos)
    else:
        st.info("nenhum aluno cadastrado")