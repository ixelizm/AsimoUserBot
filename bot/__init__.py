from pyrogram import Client
from requests import get
from bot.config import *
import time

asimo = Client(
  name = "asimo",
  api_id = API_ID,
  api_hash = API_HASH,
  session_string = SESSION_STRING,
  workers = 24,
  sleep_threshold = 60
)

url = PLUGIN_URL + "/api"
r = get(url)
data = r.json()

HELP = {}
for file, content in data.items():
  with open(f"bot/modules/{file}.py", "w") as f:
    f.write(content)
  print(file, "Plugini Yüklendi!")
asimo.plugins = dict(root="bot/modules")
starttime = time.time()
