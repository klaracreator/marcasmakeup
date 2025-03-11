import streamlit as st
import pandas as pd
import csv
import os

# Nome do arquivo CSV
csv_filename = "respostas_formulario.csv"

# Criar CSV caso não exista
def criar_csv():
    if not os.path.exists(csv_filename):
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Veias", "Acessórios", "Dificuldade Maquiagem", "Bronzeia Fácil", "Estado"])

# Função para salvar os dados
def salvar_respostas(veias, acessorios, dificuldade, bronze, estado):
    if not estado:
        st.error("Por favor, preencha o campo 'Estado'.")
        return
    
    with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([veias, acessorios, dificuldade, bronze, estado])
    
    st.success("Respostas salvas com sucesso!")

# Criar o CSV antes de iniciar o app
criar_csv()

# Estilização básica do layout
st.set_page_config(page_title="Seus tons, nossos produtos", layout="centered")

# Título do aplicativo
st.title("📋 Desenvolvendo maquiagem juntos")
st.write("Responda as perguntas abaixo para ajudar na análise de tons de pele.")

# Formulário
with st.form(key="form_tom_pele"):
    veias = st.selectbox("Qual é a cor das suas veias?", ["Azul", "Verde", "Roxa", "Outro"])
    acessorios = st.selectbox("Você prefere acessórios dourados ou prateados?", ["Dourado", "Prateado"])
    dificuldade = st.selectbox("Você tem dificuldade em achar maquiagem para você?", ["Sim", "Não"])
    bronze = st.selectbox("Você fica bronzeada com facilidade?", ["Sim", "Não", "Um pouco"])
    estado = st.text_input("Em qual estado do Brasil você mora?")

    # Botão de envio
    submit_button = st.form_submit_button("Enviar")

    if submit_button:
        salvar_respostas(veias, acessorios, dificuldade, bronze, estado)

# Exibir respostas coletadas
if os.path.exists(csv_filename):
    df = pd.read_csv(csv_filename)
    if not df.empty:
        st.subheader("📊 Dados coletados até agora")
        st.dataframe(df)
