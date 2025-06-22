import random

def generate_post(tipo, tema):
    if tipo == "Notícia":
        title = "Apple revela projeto secreto de óculos de realidade aumentada para 2026"
        body = f"""
<p>Em um movimento surpreendente, a Apple confirmou nesta semana que está desenvolvendo um novo modelo de óculos de realidade aumentada (AR)...</p>
<img src="https://source.unsplash.com/800x400/?technology,ar" style="display:block;margin:auto;">
<p>Especialistas acreditam que o dispositivo poderá revolucionar o mercado...</p>
<img src="https://source.unsplash.com/800x400/?apple,glasses" style="display:block;margin:auto;">
"""
    else:
        title = "O Quarto Trancado – Um relato real de um caso inexplicável"
        body = f"""
<p>Este relato aconteceu em 2008, na cidade de Campo Largo, PR...</p>
<img src="https://source.unsplash.com/800x400/?ghost,room" style="display:block;margin:auto;">
<p>Desde aquela noite, barulhos começaram: passos, TV ligando sozinha...</p>
<img src="https://source.unsplash.com/800x400/?haunted,doll" style="display:block;margin:auto;">
"""
    return title, body