from flask import Flask, jsonify
# from waitress import serve

from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello flask webApplication"


@app.route('/api/users')
def apiUsers():
    uus = [{"username": "admin", "email": "admin@example.com"},
           {"username": "cat", "email": "cat@example.com"}]
    return jsonify(uus)


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5001)

    # app.run(debug=False, host='0.0.0.0', port=5001)
    print("server is up on port 5001")
    http_server = WSGIServer(('', 5001), app)
    http_server.serve_forever()
