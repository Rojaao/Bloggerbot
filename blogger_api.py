import requests

# Seus dados corretos
BLOG_ID = "483973688844725319"
API_KEY = "AIzaSyBdIoALNMFS1HCZcjIlf4NvrSrL_WLHTJM"

def post_to_blogger(title, content):
    try:
        url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts?key={API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "kind": "blogger#post",
            "title": title,
            "content": content
        }
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code in [200, 201]:
            print("✅ Publicado com sucesso!")
            return True
        else:
            print(f"❌ Erro: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Erro ao publicar: {e}")
        return False
