from flask import Flask, jsonify, request
# from waitress import serve

from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello flask webApplication"


@app.route('/api/users')
def apiUsers():
    return jsonify(users)


@app.route('/api/add/user', methods=['POST'])
def addUser():
    newuser = request.get_json(silent=True)
    print(newuser)
    users.append(newuser)

    return jsonify({"name": "dog", "email": "gog@example.com"})


if __name__ == '__main__':
    users = [{"username": "admin", "email": "admin@example.com"},
             {"username": "cat", "email": "cat@example.com"}]
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5001)

    # app.run(debug=False, host='0.0.0.0', port=5001)
    print("server is up on port 5001")
    http_server = WSGIServer(('', 5001), app)
    http_server.serve_forever()
