import http.server, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
http.server.ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 8919), http.server.SimpleHTTPRequestHandler).serve_forever()
