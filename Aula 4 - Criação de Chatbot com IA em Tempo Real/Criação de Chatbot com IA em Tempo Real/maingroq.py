import streamlit as st
from groq import Groq

modelo_ia = Groq(api_key="")

st.write("# Chatbot com IA")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": texto_usuario})

    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="llama-3.3-70b-versatile"
    )

    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": texto_resposta_ia})