import streamlit as st
from services.conexao_lm_studio import conexao_com_llama
from src.script_prompt import script

# -> INTERFACE 
st.title("👵💬 Manu, sua agente financeira")

if pergunta := st.chat_input("Qual a sua dúvida sobre finanças? "):
    st.chat_message("user").write(pergunta)

    with st.spinner("🤔 A Manu está pensando..."):
        system_prompt, contexto = script()
        resposta = conexao_com_llama(system_prompt, contexto, pergunta)

    st.chat_message("assistant").write(resposta)
