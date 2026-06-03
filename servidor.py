import os
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

os.chdir("/home/thom/bkp")

# arquivos = os.listdir()

# print(arquivos[-1])
# print(arquivos[0])

PORT = 8080

server = HTTPServer(("", PORT), SimpleHTTPRequestHandler)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()
print(f"Servidor rodando na prota {PORT}")

time.sleep(4)
server.shutdown
server.server_close