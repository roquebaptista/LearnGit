from bottle import Bottle

app = Bottle(__name__)

@app.route("/")
def index():
    return '[ { "id": 1, "user": "U1232" }, { "id": 2, "user": "U1245" } ]'

if __name__ == "__main__":
    app.run(debug=True, reloader=True)