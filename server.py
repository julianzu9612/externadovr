import http.server
import socketserver
import os

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(f"Servidor iniciado en http://localhost:{PORT}")
print("Para probar en el móvil, asegúrate de estar en la misma red WiFi y usa tu IP local.")
print("Recuerda que para el móvil se requiere HTTPS (usa GitHub Pages para la ponencia).")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        httpd.server_close()
