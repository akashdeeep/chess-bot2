import http.server
import socketserver
import webbrowser

PORT = 8000  # You can change the port number if needed

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at port {PORT}")
    webbrowser.open_new_tab(f"http://localhost:{PORT}/index.html")
    httpd.serve_forever()
