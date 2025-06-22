import streamlit as st
from content_generator import generate_post
from blogger_api import post_to_blogger

st.set_page_config(page_title="AutoBlog IA", layout="wide")
st.title("🤖 Publicador Automático de Blog com IA")

tipo = st.selectbox("Tipo de conteúdo:", ["Notícia", "Conto de terror"])
tema = st.text_input("Tema ou categoria do conteúdo:", "tecnologia, mundo, mistério...")

if st.button("Gerar e Publicar"):
    with st.spinner("Gerando conteúdo..."):
        title, body = generate_post(tipo, tema)
        st.success("✅ Conteúdo gerado com sucesso!")
        st.markdown(f"### {title}")
        st.markdown(body, unsafe_allow_html=True)

        with st.spinner("Publicando no Blogger..."):
            success = post_to_blogger(title, body)
            if success:
                st.success("✅ Publicado com sucesso!")
            else:
                st.error("❌ Erro ao publicar. Verifique seu token e ID do blog.")