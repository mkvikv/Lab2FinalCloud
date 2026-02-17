from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.get("/")
def home():
    return send_from_directory("static", "index.html")

# Optional: if you later add css/images/js into static/, this will serve them too
@app.get("/<path:path>")
def static_files(path: str):
    return send_from_directory("static", path)
