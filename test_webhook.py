import requests

# Replace RENDER_URL with your actual Render deployment URL
RENDER_URL = "https://your-app-name.onrender.com"

response = requests.post(
    f"{RENDER_URL}/webhook",
    json={"event": "test", "status": "ok"}
)
print(response.json())
