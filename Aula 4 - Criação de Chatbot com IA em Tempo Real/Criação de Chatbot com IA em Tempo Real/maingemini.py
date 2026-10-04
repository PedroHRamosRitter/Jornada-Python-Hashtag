# titulo
# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar:
    # a cada mensagem que o usuario enviou no chat
    # pegar a pergunta e enviar oara a IA responder
    # exibir a resposta da IA na tela

# Streamlit -> apenas com Python criar o frontend e o backend
# Flask
# Django
# FastApi

# A ia que vamos usar: OpenAi
# pip install openai streamlit
# replit -> programacao pelo celular
# None = "não existe"
import streamlit as st
from google import genai

modelo_ia = genai.Client(api_key="")

st.write("# Chatbot com IA") #markdown

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []


texto_usuario = st.chat_input("Digite sua mensagem")
# arquivo = st.file_uploader("Selecione um arquivo")

for mensagem in st.session_state["lista_mensagens"]:
    
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)



if texto_usuario:  # O if texto_usuario: significa que se existe um valor dentro de textp usuario e verdadeiro e o if executa o print para que não fique aparecendo o none quando atualizo a página

    st.chat_message("user").write(texto_usuario)
    mensagem_usuario ={"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # Nome
    # user
    # assistant

    historico_gemini = [
        {"role": m["role"], "parts": [{"text": m["content"]}]}
        for m in st.session_state["lista_mensagens"]
    ]


    # ia respondeu
    resposta_ia = modelo_ia.models.ggenerate_content(
        contents = historico_gemini, 
        model = "gemini-2.0-flash"
    )

    texto_resposta_ia = resposta_ia.text


    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    
    
    # st.file_uploader()
# Hugging Face