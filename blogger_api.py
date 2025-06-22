import requests

# Substitua abaixo pelos seus dados:
BLOG_ID = "483973688844725319"
API_KEY = "AIzaSyBdIoALNMFS1HCZcjIlf4NvrSrL_WLHTJM"

def post_to_blogger(title, content):
    try:
        url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
        headers = {"Content-Type": "application/json"}
        params = {"key": API_KEY}
        data = {
            "kind": "blogger#post",
            "title": title,
            "content": content
        }
        response = requests.post(url, headers=headers, params=params, json=data)
        return response.status_code == 200 or response.status_code == 201
    except Exception as e:
        print(f"Erro ao publicar: {e}")
        return False
