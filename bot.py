import os
import random
import requests
import google.generativeai as genai

# Configuración de credenciales
GEMINI_KEY = os.environ["GEMINI_API_KEY"]
LI_TOKEN = os.environ["LINKEDIN_TOKEN"]
LI_URN = os.environ["LINKEDIN_URN"] # urn:li:person:uECngsyLbP

# 1. Generar contenido con Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

temas = [
    "innovación en Healthtech y telemedicina",
    "el futuro del Fintech y la inclusión financiera",
    "ciberseguridad en datos de salud",
    "cómo startups como Sereza están cambiando el panorama tecnológico",
    "la importancia de las pruebas de vulnerabilidad en sistemas financieros"
]
tema_elegido = random.choice(temas)

prompt = f"Actúa como un Technology Evangelist en la startup Sereza. Escribe un post corto y directo para LinkedIn sobre {tema_elegido}. Tono profesional, innovador y sin emojis excesivos. No uses comillas al inicio o final."

response = model.generate_content(prompt)
post_text = response.text.strip()

# 2. Publicar en LinkedIn
url = "https://api.linkedin.com/v2/ugcPosts"
headers = {
    "Authorization": f"Bearer {LI_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

payload = {
    "author": LI_URN,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": post_text},
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}

res = requests.post(url, headers=headers, json=payload)
print(f"Status: {res.status_code}")
