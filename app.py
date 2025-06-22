import streamlit as st
from content_generator import generate_post
from blogger_oauth import post_to_blogger

st.set_page_config(page_title="AutoBlog IA com OAuth", layout="wide")
st.title("🤖 AutoBlog IA – Publicador com Google OAuth")

tipo = st.selectbox("Tipo de conteúdo:", ["Notícia", "Conto de terror"])
tema = st.text_input("Tema ou categoria do conteúdo:", "tecnologia, mundo, mistério...")

if st.button("Gerar e Publicar"):
    with st.spinner("Gerando conteúdo..."):
        title, body = generate_post(tipo, tema)
        st.success("✅ Conteúdo gerado!")
        st.markdown(f"### {title}")
        st.markdown(body, unsafe_allow_html=True)

        with st.spinner("Autenticando e publicando..."):
            result = post_to_blogger(title, body)
            if result:
                st.success("✅ Publicado com sucesso no seu blog!")
            else:
                st.error("❌ Erro ao publicar no Blogger. Verifique o terminal.")