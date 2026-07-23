from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import shlex
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        longueur = int(self.headers["Content-Length"])
        data = json.loads(self.rfile.read(longueur))
        titre = data.get("titre", "")
        message = data.get("message", "")
        via = data.get("via", "python")

        try:
            if via == "c":
                subprocess.run(["notif_usb.exe", titre, message])
            else:
                cmd = [
                    "adb", "shell", "cmd", "notification", "post",
                    "-S", "bigtext",
                    "-t", shlex.quote(titre),
                    "python_notif",
                    shlex.quote(message),
                ]
                subprocess.run(cmd)
        except Exception as e:
            print("Erreur:", e)

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

HTTPServer(("localhost", 5005), Handler).serve_forever()
