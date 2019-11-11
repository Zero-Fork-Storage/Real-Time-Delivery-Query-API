from sanic import Sanic
from sanic import response
from routes import api

app = Sanic(__name__)
app.blueprint(api)

@app.route('/')
def handle_request(request):
    return response.redirect('/v1/index')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
