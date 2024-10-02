import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

SPECIES = {
    "Cyberman": "John Lumic",
    "Dalek": "Davros",
    "Judoon": "Shadow Proclamation Convention 15 Enforcer",
    "Human": "Leonardo da Vinci",
    "Ood": "Klineman Halpen",
    "Silence": "Tasha Lem",
    "Slitheen": "Coca-Cola salesman",
    "Sontaran": "General Staal",
    "Time Lord": "Rassilon",
    "Weeping Angel": "The Division Representative",
    "Zygon": "Broton"
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(self.path[2:])
        species = query.get('species', [''])[0]
        if species in SPECIES:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"credentials": SPECIES[species]}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"credentials": "Unknown"}).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8888)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()