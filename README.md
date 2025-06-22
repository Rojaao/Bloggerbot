# 🤖 AutoBlog IA com OAuth

Publicador automático para Blogger com autenticação segura via Google OAuth 2.0.

## Requisitos
- Python 3.8+
- Conta no Google com um blog no Blogger
- Ative a API do Blogger no Google Cloud
- Baixe seu `client_secret.json` da tela de credenciais

## Como usar
1. Substitua o conteúdo de `client_secret.json` com seu próprio Client ID e Client Secret
2. Rode `streamlit run app.py`
3. Faça login na sua conta Google quando solicitado
4. Clique em "Gerar e Publicar" para postar automaticamente no seu blog