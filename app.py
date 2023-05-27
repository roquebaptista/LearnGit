from bottle import Bottle

app = Bottle(__name__)

@app.route("/")
def index():
    return '{ "id": 1, "user": "u7823" }'

if __name__ == "__main__":
    app.run(debug=True, reloader=True)